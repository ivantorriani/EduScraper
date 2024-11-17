import openai 
import json
import os 
import numpy as np


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

openai.api_key = str(HEADERS["AI-Keys"]["OpenAI-3"])

# - - - - - - - - - - - - - - - - - - Example Scenario: Finding a class that matches interests

test_embedding = EMBEDDINGS["Fundamentals of Computer Science"]["desc_vector"] # Take an example 


# - - - - - - - - - - - - - - - - - -
high_mark_test = "Use algorithms to solve problems. Learn about data types and input/outputs. I also want to learn about top down design"

low_mark_test = "I want to learn Java, Python, or C++. Also, learn how to use MongoDB and other stuff."

# - - - - - - - - - - - - - - - - - - create embeddings

text_to_vector = openai.embeddings.create( 
    input = high_mark_test,
    model = "text-embedding-3-small"
)

text_to_vector2 = openai.embeddings.create(
    input = low_mark_test,
    model = "text-embedding-3-small"

)

# - - - - - - - - - - - - - - - - - - translate to vectors (remember to pull every time)


vec_1 = np.array(test_embedding)

vec_2 = np.array(text_to_vector.data[0].embedding)

vec_3 = np.array(text_to_vector2.data[0].embedding)

# - - - - - - - - - - - - - - - - - - calculate similiarity with cosine similarity


cosine_similarity1 = np.dot(vec_1, vec_2) / (np.linalg.norm(vec_1) * np.linalg.norm(vec_2)) 

cosine_similarity2 = np.dot(vec_1, vec_3) / (np.linalg.norm(vec_1) * np.linalg.norm(vec_3))

print("Good Example: " + str(cosine_similarity1)) 

print("Bad Example: " + str(cosine_similarity2))


# * Posotives: 
# * Don't have to feed huge JSON files to assistant (expensive). Instead, only return select high scoring responses.
# * We only have to use the model ONCE for big JSON, and then only for small user text responses. Cosine similiarity doesn't involve API (cheaper) 

