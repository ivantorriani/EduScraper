import json, requests
import urllib3 as lib3
from bs4 import BeautifulSoup as bs

# - - - - - - - - - - - - - - -

with open('HTML_info.json') as f:
    html_info = json.load(f)

with open('HEADERS.json') as f:
    HEADERS = json.load(f)

with open('Faculty_Information.json') as f:
    fi = json.load(f)

agent = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

j = 1

# - - - - - - - - - - - - - - - 

url = html_info["Faculty-Website"]["url"]

r = requests.get(url, headers=agent)

# - - - - - - - - - - - - - - -

soup = bs(r.text, "lxml")

table = soup.find("table")

headers = table.find_all('td')

rows = table.find_all("tr")

row_list = []

def organize_rows():
    for i in rows:
        data = i.find_all("td")
        row = [tr.text for tr in data]
        row_list.append(row)
    return row_list

rows = organize_rows()

#print(rows[1][0])

while (j < 12):
    NAME = (rows[j][0])
    TITLE = (rows[j][1])
    EMAIL = (rows[j][2])
    OFFICE = (rows[j][3])
    INTERESTS = (rows[j][4])

    entry = {
        str(NAME):{

            "NAME": str(NAME),
            "TITLE":  str(TITLE),
            "EMAIL":  str(EMAIL),
            "OFFICE": str(OFFICE),
            "INTERESTS": str(INTERESTS)
    
        }
    }
    
    with open('Faculty_Information.json', 'w') as file:
        json.dump(entry, file, indent=4)

    j += 1




#0 = NAME, #1 = TITLE, #2 = EMAIL, #3 = OFFICE, #4 = RESEARCH INTERESTS

















#web = lib3.PoolManager()

#url = html_info["Faculty-Website"]["url"]

#r = web.request('GET', url, headers=agent)

#soup = bs(r.data, 'html.parser')

#first_table = soup.find('table')

#aas = first_table.find_all('a')

#for i in aas:
    #print(i)



#[print( item.prettify() ) for item in soup.find('table') ]

