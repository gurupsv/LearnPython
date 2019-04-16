def permute(noOfCombi, data):
    if noOfCombi==1:
        return data
    else:
        return [
            x+y
            for x in permute(1, data)
            for y in permute(noOfCombi-1 , data)
        ]


print(permute(1,['a','b','c']))
print(permute(3,['a','b','c']))