from bs4 import BeautifulSoup
import requests, json

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

with open('HTML_info.json') as f:
    html_info = json.load(f)

with open('HEADERS.json') as f:
    HEADERS = json.load(f)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

def get_doc(web_url):
    url = web_url

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')

    doc = soup.prettify()

    return soup, doc


test_doc = get_doc(html_info["Faculty-Website"]["url"])[0] #Gets the HTML Doc

first_table = test_doc.find('table') #Finds the first table... kinda brute force but it works for now

#td_tag = first_table.find_all('td') #Finds all the td elements 

test = first_table.find_all('td')



def extract_content():

    td_tag_content = [test.get_text() for td in test]

    return td_tag_content

print(extract_content())

#print(td_tag)

#link_texts = [td.text for td in td_tag]

#for i in link_texts:
    
#print(test_doc.find('table', id = 'content'))


#get_doc(html_docs["Faculty-Website"]["url"]) for faculty website







