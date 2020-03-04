# pip3 install tkinter
# pip3 install requests

import tkinter  
import requests

main_window = tkinter.Tk()
main_window.geometry("450x750")
main_window.title("Crypto Checker")

# Marketcap URL
marketcap_api = "https://api.coinmarketcap.com/v1/ticker/"

# GET Marketcap
def get_marketcap(coin_name):
    web_response = requests.get(marketcap_api + coin_name)
    web_response_json = web_response.json()
    return (web_response_json[0]["market_cap_usd"])

    