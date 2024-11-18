import os, json, openai
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

HEADERS_path = os.path.abspath(
    r"C:\Documents\Computer Projects\AI-For-Data-Ethics\EduScraper\embedding\storage\headers\HEADERS.json"
)

ge_embeddings_path = os.path.abspath(
    r"C:\Documents\Computer Projects\AI-For-Data-Ethics\EduScraper\embedding\storage\embeddings\ge_embeddings.json"
)


with open(courses_path) as file:
    courses = json.load(file)

with open(ge_path) as file:
    ge = json.load(file)

with open(ge_no_desc_path) as file:
    no_desc_ge = json.load(file)

with open(HEADERS_path) as file:
    HEADERS = json.load(file)

with open(ge_embeddings_path) as file:
    ge_embeddings = json.load(file)

openai.api_key = str(HEADERS["AI-Keys"]["OpenAI-3"])



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
        print(len(id_list))
        while (i < len(id_list)):
            if course["id"] == id_list[i]:
                #des_ids.append(all_ge_ids[i])
                #descriptions.append(course["desc"])
                entry = {
                    str(course["displayName"]): { 
                        "ID": str(course["id"]),
                        "UNITS": str(course["units"]),
                        "DESC": str(course["desc"])
                    }
                }

                ge.update(entry)

            i += 1

    with open(ge_path, 'w') as file:
        json.dump(ge, file, indent = 4)

def embeddings():
    for course in ge:
        
        text_to_vector = openai.embeddings.create(
            input = str(ge[course]["DESC"]),
            model = "text-embedding-3-small"
        )

        entry = {
            str(course): {
                "desc_text": str(ge[course]["DESC"]),
                "desc_vector": text_to_vector.data[0].embedding
            }
        }

        ge_embeddings.update(entry)

    with open(ge_embeddings_path, 'w') as file:
        json.dump(ge_embeddings, file, indent = 4)



embeddings()


