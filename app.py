import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
import spacy
import streamlit as st
import yfinance as yf

nlp = spacy.load("en_core_web_sm")

st.title("Buzzing Stocks :zap:")

def extract_text_from_rss(link):
    """
    * parse xml using bs4
    * extract headlines from link
    * append to headings

    """

    headings = []
    r1 = requests.get("https://economictimes.indiatimes.com/markets/rssfeeds/1977021501.cms")
    r2 = requests.get(link)
    soup1 = BeautifulSoup(r1.content, 'lxml')
    soup2 = BeautifulSoup(r2.content, 'lxml')
    print("created Soup\n\n")

    headings1 = soup1.find_all('title')
    headings2 = soup2.find_all('title')
    print("found title\n\n")
    headings = headings1+headings2
    headings = headings2

    return headings

token_dict = {
    'Org': [],
    'Symbol': [],
    'currentPrice': [],
    'dayHigh': [],
    'dayLow': [],
    'forwardPE': [],
    'dividendYield': []
}


def extract_stock_info(headings):
    """
    * Goes over each heading in list
    * extract entites using nlp pipeline
    * match entities with csv data [link csv and entities]
    * Get company name, symbol, stats
    * return: DataFrame, to be displayed onto Streamlit Dashboard
    
    """
    print("starting stock info extraction")
    stocks_df = pd.read_csv("./data/ind_nifty500list.csv")

    for title in headings[0]:
        doc = nlp(title.text)
        # using ents from each element of doc 

        for token in doc.ents:
            try:
                if stocks_df['Company Name'].str.contains(token.text).sum():

                    symbol = stocks_df[stocks_df['Company Name'].str.contains(token.text)]['Symbol'].values[0]
                    org_name = stocks_df[stocks_df['Company Name'].str.contains(token.text)]['Company Name'].values[0]
                    token_dict['Symbol'].append(symbol)
                    token_dict['Org'].append(org_name)
                    # debug string
                    print(symbol+".NS")
                    # send to yfinance for stats retrieval
                    stock_info = yf.Ticker(symbol+".NS").info
                    token_dict['currentPrice'].append(stock_info['currentPrice'])
                    token_dict['dayHigh'].append(stock_info['dayHigh'])
                    token_dict['dayLow'].append(stock_info['dayLow'])
                    token_dict['forwardPE'].append(stock_info['forwardPE'])
                    token_dict['dividendYield'].append(stock_info['dividendYield'])

                else:
                    pass
            except:
                pass

    output_df = pd.DataFrame(token_dict)
    return output_df

# STREAMLIT DASHBOARD 

## adding input field
user_input = st.text_input("Add RSS link here!" , "https://www1.nseindia.com/products/content/equities/indices/nifty_500.htm")

## get the heading
heading_list = extract_text_from_rss(user_input)

# debug string
print(heading_list)

## output financial stats through a dataFrame
output_DF = extract_stock_info(heading_list)
output_DF.drop_duplicates(inplace=True)

st.dataframe(output_DF)

## displaying headlines as a separate div
st.subheader("Headlines")
with st.expander("Expand for Headlines ! :sunflower:"):
    for h in heading_list:
        st.markdown("* " + h.text)
