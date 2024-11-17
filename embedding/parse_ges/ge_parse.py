import os, json
from halo import Halo as hl
i = 0 
# - - - - - - - - - - - - - - - - -

courses_path = os.path.abspath(

    r"C:\Documents\Computer Projects\AI-For-Data-Ethics\EduScraper\data\2022-2026.json"

)


ge_path = os.path.abspath(

    r"C:\Documents\Computer Projects\AI-For-Data-Ethics\EduScraper\data\ge.json"
)

ge_no_desc_path = os.path.abspath(
    r"C:\Documents\Computer Projects\AI-For-Data-Ethics\EduScraper\data\2022-2026-GE.json"

)


with open(courses_path) as file:
    courses = json.load(file)

with open(ge_path) as file:
    ge = json.load(file)

with open(ge_no_desc_path) as file:
    no_desc_ge = json.load(file)


all_ge_ids = []
des_ids = []
descriptions = []

spinner = hl(text='Loading', spinner='dots')

# - - - - - - - - - - - - - - - - -
def get_ges_by_id():
    for course in no_desc_ge:
        all_ge_ids.append(course["id"])
    return all_ge_ids
    
id_list = get_ges_by_id()

def match():

    for course in courses:
        i = 0
        while (i < len(id_list)):
            if course["id"] == id_list[i]:
                des_ids.append(all_ge_ids[i])
                descriptions.append(course["desc"])
            i += 1
    
    print(descriptions)

match()   