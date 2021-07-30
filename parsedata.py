import json
with open('songData.json') as json_data:
    jsonData = json.load(json_data)
print(jsonData)