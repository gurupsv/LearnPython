import json
fo=open("first.json","r")
data = json.load(fo)
print(type(data))
print(data)
fo.close()