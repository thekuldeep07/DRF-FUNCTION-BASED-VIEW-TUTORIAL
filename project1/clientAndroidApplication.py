import requests
import json

URL ="http://127.0.0.1:8000/createStudent/"


def post():
    data={
    'name':'kuldeep',
    'rollNo':12,
    'address':'gurgaon'
}
    json_data = json.dumps(data)
    response = requests.post(url = URL,data =json_data)
    data = response.json()
    print(data)

def update():
    data={
    'id':2,
    'name':'kuldeepUpdate',
    'rollNo':12,
    'address':'gurgaon'}
    json_data = json.dumps(data)
    r = requests.put(url=URL,data=json_data)
    data = r.json()
    print(data)

def delete():
    data={
        'id':2}
    json_Data = json.dumps(data)
    r=requests.delete(url=URL,data=json_Data)
    data = r.json()
    print(data)
delete()



