import json

def read(jsondata):
    with open(jsondata, 'r') as rd:
        data = json.load(rd)
        return data

def write(jsondata, data):
    with open(jsondata, 'w') as wr:
        json.dump(data, wr)