import json


file = open('canary.log', 'r')
while True:
    line = file.readline()
    if not line:
        break
    print(json.loads(line)["log"].rstrip())