*To Run this application you will need both Node and FLask installed onto your device *

*To Install Nodejs please go to https://nodejs.org/en/download/ and to install Flask please go to https://flask.palletsprojects.com/en/2.0.x/installation/ *

---

# BTC/ETH Exchange Rate APP (Svelte +FLask)

This project is a web app that is built using Svelte.js for the front end and Flask(Python) for the back end. The purpose of this application is to fetch the data from two different sources for both Bitcoin and Ethereum and displays both buy and sell price for both sources. The application will also recommend the user on which exchange source to trade on along with the price difference between sources.

<img width="1674" alt="Screen Shot 2021-10-18 at 1 26 46 AM" src="https://user-images.githubusercontent.com/86750392/137673883-b85c600c-5c80-4078-bc00-9e3b0c968a73.png">

<img width="1677" alt="Screen Shot 2021-10-18 at 1 26 55 AM" src="https://user-images.githubusercontent.com/86750392/137673895-cf97e5c3-f8ed-41b5-a3e6-f135be678d38.png">


*Note that you will need to have [Node.js] and [Flask(Python)] installed. *

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


## now you are ready to run:



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

Navigate to [localhost:5000](http://localhost:5000). You should see your app running.

if you see this when running the app

<img width="748" alt="Screen Shot 2021-10-18 at 1 29 21 AM" src="https://user-images.githubusercontent.com/86750392/137674643-bc50658b-eaa0-452a-b270-7b66ca45387d.png">

the fix is easy all you need to do is 

end the server
```bash
    ctrl + C 
```
then
```bash
    export FLASK_APP=server.py
    export FLASK_ENV=development
    flask run
```
after this you will see something similar to this

<img width="419" alt="Screen Shot 2021-10-18 at 1 38 33 AM" src="https://user-images.githubusercontent.com/86750392/137674841-15d0d493-e418-48fb-aa48-a05ff77af97a.png">


you can now run the server again and it will run similar to this

<img width="580" alt="Screen Shot 2021-10-18 at 1 41 51 AM" src="https://user-images.githubusercontent.com/86750392/137675173-494d0bf9-eb99-4ca1-836e-4debf244a69a.png">









