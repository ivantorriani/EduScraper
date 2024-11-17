import openai 
import json
import os 

course_info_path = os.path.abspath(

    r"C:\Documents\Computer Projects\AI-For-Data-Ethics\Vector-Embedding\storage\info\course_info.json"
)

faculty_info_path = os.path.abspath(
    r"C:\Documents\Computer Projects\AI-For-Data-Ethics\Vector-Embedding\storage\info\Faculty_Information.json"
)

embeddings_path = os.path.abspath(
    r"C:\Documents\Computer Projects\AI-For-Data-Ethics\Vector-Embedding\storage\embeddings\course_embeddings.json"
)

HEADERS_path = os.path.abspath(
    r"C:\Documents\Computer Projects\AI-For-Data-Ethics\Vector-Embedding\storage\headers\HEADERS.json"
)
with open(course_info_path) as file:
    course_info = json.load(file)

with open(faculty_info_path) as file:
    faculty_info = json.load(file)

with open(HEADERS_path) as file:
    HEADERS = json.load(file)

with open(embeddings_path) as file:
    EMBEDDINGS = json.load(file)

# - - - - - - - - - - - - - -

openai.api_key = str(HEADERS["AI-Keys"]["OpenAI-3"])

# - - - - - - - - - - - - - -




def embed_info():
    EMBEDDINGS = {}
    for i in course_info:

        text_to_vector = openai.embeddings.create(
            input = str((course_info[str(i)]["DESCRIPTION"])),
            model = "text-embedding-3-small"
        )


        entry = {
            str(i): {
                "desc_text": str(course_info[str(i)]["DESCRIPTION"]),
                "desc_vector": text_to_vector.data[0].embedding
            }
        }

        EMBEDDINGS.update(entry)

    with open(embeddings_path, 'w') as file:
        json.dump(EMBEDDINGS,file, indent=4)

