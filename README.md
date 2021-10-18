*To Run this application you will need both Nodejs and FLask(python) and Requests(python) installed onto your device *

*To Install Nodejs please go to https://nodejs.org/en/download/ and to install Flask please go to https://flask.palletsprojects.com/en/2.0.x/installation/ and to install Requests please go to https://pypi.org/project/requests/ *

*Questionare answers in question.md *
---

# BTC/ETH Exchange Rate APP (Svelte +FLask)

This project is a web app that is built using Svelte.js for the front end and Flask(Python) for the back end. The purpose of this application is to fetch the data from two different sources for both Bitcoin and Ethereum and displays both buy and sell price for both sources. The application will also recommend the user on which exchange source to trade on along with the price difference between sources.

<img width="1656" alt="Screen Shot 2021-10-18 at 3 39 29 PM" src="https://user-images.githubusercontent.com/86750392/137795915-f2df41b7-06c5-4a7c-a019-0ca441b8115f.png">


<img width="1669" alt="Screen Shot 2021-10-18 at 3 39 37 PM" src="https://user-images.githubusercontent.com/86750392/137795925-9e1325a0-fdf5-4d45-9be7-accf700ebc82.png">

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

*To Install Waitress please go to https://pypi.org/project/waitress/ *

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




