# Load dependencies
from bs4 import BeautifulSoup
import requests
import json
import time
import random
import os
import sys
import webbrowser

sys.setrecursionlimit(9999)

# Get the url from terminal
url = sys.argv[1]

# Extract JSON info
def check_ticketswap_offers(url, counter = 0):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    ldjson_soup = soup.findAll("script", attrs = {'type':"application/json"})
    ldjson_str = ldjson_soup[0].text
    ldjson = json.loads(ldjson_str)
    if int(ldjson['props']['pageProps']['data']['node']['availableTicketsCount']) < 1:
        seconds = random.randrange (75, 125) / 100
        time.sleep(seconds)
        counter += 1
        print("Try %s" % counter)
        return check_ticketswap_offers(url, counter)
    path = ldjson['props']['pageProps']['data']['node']['event']['types']['edges'][0]['node']['availableListings']['edges'][0]['node']['uri']['path'].split('?')[0]
    url_open = "https://ticketswap.nl" + path
    webbrowser.get('chrome').open_new(url_open)

# Run ticketswapper
check_ticketswap_offers(url)