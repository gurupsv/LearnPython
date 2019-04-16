d=[
    {"fname": "Sachin", "lname": "Tendulkar"},
    {"fname": "Saurav", "lname": "Ganguly"},
    {"fname": "Rahul", "lname": "Dravid"},
    {"fname": "Yuvraj", "lname": "Singh"},
    {"fname": "Anil", "lname": "Kumble"},
    {"fname": "Harbhajan", "lname": "Singh"}
]


def my(el):
    print("My function was called for " + el["fname"])
    return len(el["lname"]) + len(el["fname"])


d.sort(key=my, reverse=True)
for el in d:
    print(el["fname"] + " " + el["lname"])