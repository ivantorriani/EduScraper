import json

with open('training_program.json') as f:
    training_program = json.load(f)

context = (
    "You will recieve a block of unorganized table data. However, the data follows the sequence " +
    "[Name, Title, Email, Office, Research Interests]. As you parse through each data, label each " +
    "value as NAME, TITLE, OFFICE, Etc... " + 
    "See the training program for the desired output: " + 
    str(training_program["NER-Training-Program"]["Correct-Example"]) + 
    str(training_program["NER-Training-Program"]["Correct-Example2"]) + 
    str(training_program["NER-Training-Program"]["Correct-Example3"])
)

#0 = NAME, #1 = TITLE, #2 = EMAIL, #3 = OFFICE, #4 = RESEARCH INTERESTS