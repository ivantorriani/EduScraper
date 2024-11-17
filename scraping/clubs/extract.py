import json, requests, os
import urllib3 as lib3
from bs4 import BeautifulSoup as bs

# - - - - - - - - - - - - - - - - - - - -

path_HEADERS = os.path.abspath(
    r"C:\Documents\Computer Projects\AI-For-Data-Ethics\EduScraper\secrets\HEADERS.json"
)

path_HTML_INFO = os.path.abspath(
    r"C:\Documents\Computer Projects\AI-For-Data-Ethics\EduScraper\data\HTML_info.json"
)

# - - - - - - - - - - - - - - - - - - - -

with open(path_HTML_INFO) as f:
    HTML_INFO = json.load(f)

with open(path_HEADERS) as f:
    HEADERS = json.load(f)

agent = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# - - - - - - - - - - - - - - - - - - - -

url = HTML_INFO["Clubs-Website"]["url"]

r = requests.get(url, headers=agent)

# - - - - - - - - - - - - - - - - - - - -

soup = bs(r.text, "lxml")

print(soup.prettify())

