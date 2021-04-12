import datetime

from bs4 import BeautifulSoup
import requests
keyword = '롤린'

mozhdr = { 'User-Agent': 'Mozilla / 5.0 (Windows; U; Windows NT 5.1; en-GB; rv : 1.9.0.3) Gecko / 2008092417 Firefox / 3.0.3'}

scrape_url="https://www.youtube.com"
search_url="/results?search_query="
search_hardcode = "롤린+lyrics"

sb_url = scrape_url + search_url + search_hardcode
sb_get = requests.get(sb_url, headers = mozhdr)
print(sb_get)
soupeddata = BeautifulSoup(sb_get.content, "html.parser")

script = soupeddata.find_all("script")
script_ = str(script[32])
print(script_)

def extract_url(tag):
    for x in tag.split(','):
        if "watch?" in x:
            return x
url_ = extract_url(script_)

url = url_.split(':')[3]
print(url[1:-1])
