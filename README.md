*To Run this application you will need both Node and FLask installed onto your device *

*To Install Nodejs please go to https://nodejs.org/en/download/ and to install Flask please go to https://flask.palletsprojects.com/en/2.0.x/installation/*

---

# BTC/ETH Exchange Rate APP (Svelte +FLask)

This project is a web app that is built using Svelte.js for the front end and Flask(Python) for the back end. The purpose of this application is to fetch the data from two different sources for both Bitcoin and Ethereum and displays both buy and sell price for both sources. The application will also recommend the user on which exchange source to trade on along with the price difference between sources.

*Note that you will need to have [Node.js] and [Flask(Python)] installed.*

## Exchange Sources

For Bitcoin:
https://www.bitfinex.com and 
https://www.blockchain.com
for Ethereum:
https://www.bitfinex.com and 
https://www.kraken.com

## How It Works

The backend consists of 4 Api's that call onto its corresponding exchange rate api to fetch the exchange rate data in json format. The fron end calls on the backend api's and retreives the exchange rate data. The front end then parses the data and displays it accordingly.

## Get started

Download the Project

```bash
git clone https://github.com/humzahokadia/BTC-ETH-Exchange-Rate-APP-Svelte-Flask-.git
```

next navigate to the folder

```bash
cd BTC-ETH-Exchange-Rate-APP-Svelte-Flask-
```


###now you are ready to run:



first start the server 

```bash
python server.py
```

next navigate to the public folder

```bash
cd public
```

next install dependencies 

```bash
npm install
```

and finally deploy the front end

```bash
npm run build 
```

The application is now running...

Navigate to [localhost:5000](http://localhost:5000). You should see your app running. Edit a component file in `src`, save it, and reload the page to see your changes.

