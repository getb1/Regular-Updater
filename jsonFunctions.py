import json


def write(dictionary, file, mode):
    with open(file, mode) as file:
        file.write(json.dumps(dictionary))


def read(file):
    with open(file, "r") as file:
        contents = file.read()
        contents = json.loads(contents)
        return contents
