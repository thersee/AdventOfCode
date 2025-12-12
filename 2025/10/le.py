import json 
import re

with open('10/leaderboard.json') as f:
    data = f.read()
data = json.loads(data)

numberQualified = 0
for d in data["members"]:
    vals = data["members"][d]
    if int(vals["stars"]) >= 10:
        numberQualified += 1
print(numberQualified)