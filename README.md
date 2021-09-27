
![Logo](https://cdn-images-1.medium.com/max/1024/1*u9U3YjxT9c9A1FIaDMonHw.png)

    
# Hot Stocks Newsfeed

**A Streamlit WebApp that uses:**

* spacy(NLP) for Named Entitry Recognitition[NER]
* request, BeautifulSoup to parse the scraped Content
* Streamlit - Open-source Python Library for creating custom WebApps
* Yahoo-finance API




## API Reference

pip install yfinance

#### Get item

```http
  GET /api/items/${Ticker_Symbol}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Ticker_Symbol`      | `string` | **Stock Stats Retrieval** |

  
## Run Locally

Clone the project

```bash
  git clone https://github.com/Srikanthpai5/HotStocks_NewsFeed
```

Go to the project directory

```bash
  cd HotStocks_NewsFeed
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  streamlit run app.py
```

  
## Documentation

* [Streamlit](https://docs.streamlit.io/en/stable/)

* [Spacy NLP](https://spacy.io/usage)
