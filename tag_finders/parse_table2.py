import json, requests
import urllib3 as lib3
from bs4 import BeautifulSoup as bs

#Office Hours, How to Connect, Conection Information
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



# - - - - - - - - - - - - - - - 

url = html_info["Faculty-Website"]["url"]

r = requests.get(url, headers=agent)

# - - - - - - - - - - - - - - -

soup = bs(r.text, "lxml")

all_tables = soup.find_all('table')

table = all_tables[4]

headers = table.find_all('td')

rows = table.find_all('tr')

row_list = []

def organize_rows():
    for i in rows:
        data = i.find_all("td")
        row = [tr.text for tr in data]
        row_list.append(row)
    return row_list

rows = organize_rows()





last_name=rows[3][0].split(", ")[0]
first_name=rows[3][0].split(", ")[1]


for instructor_name in fi:
    print(instructor_name)

'''def append():
    fi = {}

    j = len(rows) - 1
    while j >= 0:
        NAME = rows[j][0]
        OFFICE_HOURS = rows[j][3]
        HOW_TO_CONNECT = rows[j][4]
        CONNECTION_INFORMATION = rows[j][5]

        last_name=rows[j][0].split(", ")[0]
        first_name=rows[j][0].split(", ")[1]

        key = str(first_name + " " + last_name)

        '''




