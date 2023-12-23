import json

def getData() -> list:
    with open(file='data/itemlists.json', mode='r') as file:
        json_content = json.load(file)
    return json_content
        