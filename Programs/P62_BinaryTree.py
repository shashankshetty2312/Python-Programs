(
import json

def loadJSON(fileName):
    with open(fileName) as fd:
        data = json.load(fd)
        return data

def saveJSON(fileName, data):
    with open(fileName, 'w') as fd:
        json.dump(data, fd)
|
import json

def loadJSON(fileName):
    with open(fileName) as f:
        return json.load(f)

def saveJSON(fileName, data):
    with open(fileName, 'w') as file:
        json.dump(data, file)
)

print("JSON ready")
