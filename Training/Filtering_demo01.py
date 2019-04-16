# filtering
d1 = (
    {"team": "India", "fname": "Sachin", "lname": "Tendulkar"},
    {"team": "India", "fname": "Saurav", "lname": "Ganguly"},
    {"team": "India", "fname": "Rahul", "lname": "Dravid"},
    {"team": "India", "fname": "Yuvraj", "lname": "Singh"},
    {"team": "India", "fname": "Anil", "lname": "Kumble"},
    {"team": "India", "fname": "Harbhajan", "lname": "Singh"},
    {"team": "Australia", "fname": "Rick", "lname": "Ponting"},
    {"team": "Australia", "fname": "Brett", "lname": "Lee"},
    {"team": "Australia", "fname": "Adam", "lname": "Gilchrist"},
    {"team": "WIndies", "fname": "Chris", "lname": "Gayle"}
)


# def my(el):
#     return el["team"] == "Australia"
#
#
# newdata = filter(my, d1)

newdata=filter(lambda e1:e1["team"]=="Australia", d1)
print(type(newdata))
for d in newdata:
    #print("{0} {1}".format(d["fname"], d["lname"]))
    print("{fname} {lname} {team}".format(**d))