import json
from parse_divs1 import(
    get_coursenum,
    get_course_title,
    get_course_units,
    get_course_prereq,
    get_course_description
)

# - - - - - - - - - - - - - - - - 

course_numbers = get_coursenum()
course_titles = get_course_title()
course_units = get_course_units()
course_prereq = get_course_prereq()
course_description = get_course_description()

with open('course_info.json') as f:
    COURSE_INFO = json.load(f)

# - - - - - - - - - - - - - - - - 

print(len(course_numbers), len(course_titles), len(course_units), len(course_prereq), len(course_description))