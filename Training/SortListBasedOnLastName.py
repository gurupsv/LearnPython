d=[
    ["Sachin","Tendulkar"],
    ["Saurav","Ganguly"]  ,
    ["Rahul","Dravid"],
    ["Yuvraj","Singh"],
    ["Anil","Kumble"],
    ["Harbhajan","Singh"]
   ]

# def my(e1):
#     return(len(e1[1]))
#
# d.sort(key=my)

d.sort(key=lambda e1:len(e1[1]))
print(d)

for el in d:
    print(el[0] + " " + el[1])