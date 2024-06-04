import pandas as pd
import requests
from bs4 import BeautifulSoup
url="https://www.sec.gov/edgar/browse/?CIK=789019&owner=exclude"

headers=({"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":'en-US,en;q=0.5'})
page=requests.get(url,headers=headers)
soup=BeautifulSoup(page.text,"html")
print(soup)