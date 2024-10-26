import json, requests
import urllib3 as lib3
from bs4 import BeautifulSoup as bs

# - - - - - - - - - - - - - - -

with open('HTML_info.json') as f:
    html_info = json.load(f)

with open('HEADERS.json') as f:
    HEADERS = json.load(f)

agent = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# - - - - - - - - - - - - - - - 

url = html_info["Faculty-Website"]["url"]

r = requests.get(url, headers=agent)

# - - - - - - - - - - - - - - -

soup = bs(r.text, "lxml")

table = soup.find("table")

headers = table.find_all('td')

rows = table.find_all("tr")

row_list = []
for i in rows:
    data = i.find_all("td")
    row = [tr.text for tr in data]
    row_list.append(row)
    

print(row_list[0])

















#web = lib3.PoolManager()

#url = html_info["Faculty-Website"]["url"]

#r = web.request('GET', url, headers=agent)

#soup = bs(r.data, 'html.parser')

#first_table = soup.find('table')

#aas = first_table.find_all('a')

#for i in aas:
    #print(i)



#[print( item.prettify() ) for item in soup.find('table') ]

