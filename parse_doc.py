from grab_html_doc import (
    get_doc,
    extract_content,
)

from params import context

import requests, json, os
import google.generativeai as genai 

# - - - - - - - - - - - - - - -


with open('HTML_info.json') as f:
    html_info = json.load(f)

with open('HEADERS.json') as f:
    HEADERS = json.load(f)

with open('Faculty-Information.json') as f:
    fi = json.load(f)


genai.configure(api_key=(HEADERS["AI-Keys"]["GeminiAI"]))

client = genai.GenerativeModel("gemini-1.5-flash")

#cache = {"context": context, "ttl": 3600}



# - - - - - - - - - - - - - - -

test_doc = get_doc(html_info["Faculty-Website"]["url"])[0] #Gets the HTML Doc

first_table = test_doc.find('table') #Finds the first table... kinda brute force but it works for now

td_tag = first_table.find_all('td') #Finds all the td elements 

extracted_content = extract_content()

i = 0
j = 0

user_message = extracted_content

payload = {
    "input": str(user_message),
    "context": str(context)
}

response = client.generate_content(
    str(payload["context"]) + str(payload["input"])
)

print(response)


#0 = NAME, #1 = TITLE, #2 = EMAIL, #3 = OFFICE, #4 = RESEARCH INTERESTS


#while (i <= len(extracted_content)):
    #while (j <= len(data)):


'''
if (j == 0):
    key = data[j]

    entry = {
        str(key):{
            "Happy, happy, happy!"
        }
    }

    with open('Faculty-Information.json', 'w') as file:
        json.dump(fi, file)

    j += 1'''

#new_faculty_member = { #this format is kinda nice
    #"name": "John Doe",
    #"department": "Mathematics",
    #"email": "johndoe@example.com"
#



    
        



# Name | Title | Email | Office | Research Interests | Office Hours | How to Connect | Connect Information