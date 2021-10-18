*To Run this application you will need both Node and FLask installed onto your device *

*To Install Nodejs please go to https://nodejs.org/en/download/ and to install Flask please go to https://flask.palletsprojects.com/en/2.0.x/installation/ *

*Questionare answers in question.md *
---

# BTC/ETH Exchange Rate APP (Svelte +FLask)

This project is a web app that is built using Svelte.js for the front end and Flask(Python) for the back end. The purpose of this application is to fetch the data from two different sources for both Bitcoin and Ethereum and displays both buy and sell price for both sources. The application will also recommend the user on which exchange source to trade on along with the price difference between sources.

<img width="1674" alt="Screen Shot 2021-10-18 at 1 26 46 AM" src="https://user-images.githubusercontent.com/86750392/137673883-b85c600c-5c80-4078-bc00-9e3b0c968a73.png">

<img width="1677" alt="Screen Shot 2021-10-18 at 1 26 55 AM" src="https://user-images.githubusercontent.com/86750392/137673895-cf97e5c3-f8ed-41b5-a3e6-f135be678d38.png">


*Note that you will need to have [Node.js] and [Flask(Python)] installed. *

## Exchange Sources

For Bitcoin:

https://www.bitfinex.com 


https://www.blockchain.com


for Ethereum:

https://www.bitfinex.com 


https://www.kraken.com

## How It Works

The backend consists of 4 Api's that call onto its corresponding exchange rate api to fetch the exchange rate data in json format. The fron end calls on the backend api's and retreives the exchange rate data. The front end then parses the data and displays it accordingly.

## Get started
*These installation an Deployment Instructions are meant for MAC OS *
Download the Project

```bash
git clone https://github.com/humzahokadia/BTC-ETH-Exchange-Rate-APP-Svelte-Flask-.git
```

next navigate to the folder

```bash
cd BTC-ETH-Exchange-Rate-APP-Svelte-Flask-
```


# How To Run:

## To Run With Development Server:

first set up the environment 
```bash
    export FLASK_APP=server.py
    export FLASK_ENV=development
    flask run
```

then start the server 

```bash
python server.py
```
in a new terminal tab navigate to the public folder

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

Navigate to [localhost:5000](http://localhost:5000).

<img width="580" alt="Screen Shot 2021-10-18 at 1 41 51 AM" src="https://user-images.githubusercontent.com/86750392/137675173-494d0bf9-eb99-4ca1-836e-4debf244a69a.png">

## To Run With Production Server:

*To Run this application with a production server you will need Waitress(python) installed onto your device *

first start the server 

```bash
python server2.py
```
in a new terminal tab navigate to the public folder

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

Navigate to [localhost:8080](http://localhost:8080). 

or

Navigate to [0.0.0.0:8080](http://0.0.0.0:8080).


<img width="333" alt="Screen Shot 2021-10-18 at 2 06 08 AM" src="https://user-images.githubusercontent.com/86750392/137677670-0385d41f-1c31-42b0-aa62-d538d2197bca.png">




