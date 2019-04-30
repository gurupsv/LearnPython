
import json
resp='''
    [
{"id":1,"fname":"Sachin","lname":"Tendulkar"},
{"id":2,"fname":"Saurav","lname":"Ganguly"},
{"id":3,"fname":"Rahul","lname":"Dravid"},
{"id":4,"fname":"Yuvraj","lname":"Singh"}
]
    '''
print(type(resp))
data = json.loads(resp)
print(type(data))
print(data)