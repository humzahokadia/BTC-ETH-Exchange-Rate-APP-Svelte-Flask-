from flask import Flask, send_from_directory
import random
import requests
app = Flask(__name__)#apis for site
# Path for our main Svelte page
@app.route("/")#connect front and backend so when you run server the entire application is ran
def base():
    return send_from_directory('public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('public', path)

@app.route("/btc")#api to get first bitcoin buy/sell prices
def btc1():
    url = "https://api.bitfinex.com/v1/pubticker/btcusd"
    response = requests.request("GET", url)
    return(response.text)

@app.route("/btc2")#api to get second bitcoin buy/sell prices
def btc2():
    url = "https://blockchain.info/ticker"
    response = requests.request("GET", url)
    return(response.text)

@app.route("/eth")#api to get first ethereum buy/sell prices
def eth1():
    url = "https://api.bitfinex.com/v1/pubticker/ethusd"
    response = requests.request("GET", url)
    return(response.text)

@app.route("/eth2")#api to get second ethereum buy/sell prices
def eth2():
    url = "https://api.kraken.com/0/public/Ticker?pair=ETHUSD"
    response = requests.request("GET", url)
    return(response.text)

if __name__ == "__main__":
   from waitress import serve
   serve(app, host="0.0.0.0", port=8080)
