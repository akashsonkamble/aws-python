import json

def readJsonFile(fileName):
    data = ""
    try:
        with open('files/lab14_insulin.json') as json_file:
            data = json.load(json_file)
    except IOError:
        print("Could not read file")
    return data