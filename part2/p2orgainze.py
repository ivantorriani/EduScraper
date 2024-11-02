import json
from parse_divs1 import(
    get_coursenum,
    get_course_title,
    get_course_units,
    get_course_prereq,
    get_course_description
)

# - - - - - - - - - - - - - - - - 

#courseNumber | units | courseTitle | Prerequisite | summary

course_numbers = get_coursenum()
course_titles = get_course_title()
course_units = get_course_units()
course_prereq = get_course_prereq()
course_description = get_course_description()

official_len = len(course_numbers)

with open('course_info.json') as f:
    COURSE_INFO = json.load(f)

# - - - - - - - - - - - - - - - - 

i = 0

def organize():
    global i
    while (i < len(course_numbers)):
        COURSE_NUM = course_numbers[i]
        UNITS = course_numbers[i]
        COURSE_TITLE = course_titles[i]
        COURSE_PREREQ = course_prereq[i]
        COURSE_DESC = course_description[i]

        entry = {
            str(COURSE_TITLE): {
                "NUMBER": str(COURSE_NUM),
                "UNITS": str(UNITS),
                "TITLE": str(COURSE_TITLE),
                "PREREQUISITE": str(COURSE_PREREQ),
                "DESCRIPTION": str(COURSE_DESC)
            }
        }

        COURSE_INFO.update(entry)
        i += 1
    with open('course_info.json', 'w') as file:
        json.dump(COURSE_INFO, file, indent=4)


organize()




