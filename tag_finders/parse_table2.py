import json, requests
import urllib3 as lib3
from bs4 import BeautifulSoup as bs
from halo import Halo as hlo

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

o_t_spinner = hlo(text = 'Organizing?', spinner = 'line')


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


last_name=rows[2][0].split(", ")[0]
first_name=rows[2][0].split(", ")[1]

for i in fi:
    if (str(first_name + " " + last_name)) == i:
        print(i)
        print(str(first_name + " " + last_name))







def append_please():
    fi = {}

    j = len(rows) - 1
    while j >= 0:

        o_t_spinner.start()

        NAME = rows[j][0]
        OFFICE_HOURS = rows[j][3]
        HOW_TO_CONNECT = rows[j][4]
        CONNECTION_INFORMATION = rows[j][5]

        try:
            last_name=NAME.split(", ")[0]
            first_name=NAME.split(", ")[1]
        except IndexError:
            continue

        key = str(first_name + " " + last_name)

        for names in fi:
            if names == key:
                entry = {
                    "OFFICE-HOURS": str(OFFICE_HOURS),
                    "HOW-TO-CONNECT": str(HOW_TO_CONNECT),
                    "CONNECTION-INFORMATION": str(CONNECTION_INFORMATION)
                }

                fi[key].update(entry)

        j -= 1

    o_t_spinner.succeed('Text data gathered successfuly')
    
    with open('Faculty_Information.json', 'w') as file:
        json.dump(fi, file, indent=4)


append_please()


        




