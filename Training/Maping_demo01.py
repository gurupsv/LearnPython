data=(13,3,44,58,32,15,39)

# def my(e1):
#     return e1*2
#
# newdata=map(my,data)

newdata=map(lambda e1:e1*2/3, data)
for d in newdata:
    print(d)

