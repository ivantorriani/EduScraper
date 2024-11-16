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

#courseNumber | units | courseTitle | Prerequisite | summary

course_numbers = []
course_num_final = []
course_units = []
course_title = []
prerequisite = []
summary = []


# - - - - - - - - - - - - - - - 

url = html_info["Courses-Website"]["url"]

r = requests.get(url, headers=agent)

# - - - - - - - - - - - - - - -

soup = bs(r.text, "lxml")

block = soup.find('div', class_ = 'sc_sccoursedescs')

course_blocks = block.find_all('div', class_ = 'courseblock')


def get_coursenum():
    temp_holder = []
    for i in course_blocks:
        number_slot = i.find('p', class_ = 'courseblocktitle')
        temp_holder.append(number_slot.get_text())
    for j in temp_holder:
        error_tag = j.split(". ")[0][-3:]
        course_numbers.append(error_tag)

    temp_holder = []
    return course_numbers

def get_course_title():
    temp_holder = []
    for i in course_blocks:
        title_slot = i.find('p', class_ = 'courseblocktitle')
        temp_holder.append(title_slot.get_text())
    for j in temp_holder:
        title_tag = j.split(". ")[1]
        title = title_tag.split(".")[0]
        course_title.append(title)
    
    temp_holder = []
    return course_title

def get_course_units():
    for i in course_blocks:
        unit_slot = i.find('span', class_ = "courseblockhours")
        units = unit_slot.get_text().split("\n")[0]
        course_units.append(units)
    return course_units
    
def get_course_prereq():
    temp_holder = []
    for i in course_blocks:
        prereq_area = i.find('div', class_ = 'noindent courseextendedwrap')
        prereq_slot = prereq_area.find_all('p')
        for j in prereq_slot:
            if j.get('class') == None:
                temp_holder.append(j)
    for i in temp_holder:
        prereqs = (i.get_text())
        prerequisite.append(prereqs)

    return prerequisite

def get_course_description():
    for i in course_blocks:
        desc_area = i.find('div', class_ = 'courseblockdesc')
        desc_slot = desc_area.find('p')
        summary.append(desc_slot.get_text())
    return summary

