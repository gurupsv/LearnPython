myprodlist=[
    {"pid":12101,"name":"Redmi Note 7","cost":12000,"brand":"mi","category":"mobile","rating":5,"discount":0},
    {"pid":12102,"name":"Nokia 7.1","cost":115000,"brand":"nokia","category":"mobile","rating":4,"discount":10},
    {"pid":12103,"name":"Samsung Galaxy 10","cost":72000,"brand":"samsung","category":"mobile","rating":1,"discount":20},
    {"pid":12104,"name":"iphone XS Max","cost":92000,"brand":"apple","category":"mobile","rating":5,"discount":0},
    {"pid":12105,"name":"Mac Book Pro","cost":212000,"brand":"apple","category":"laptop","rating":5,"discount":0},
    {"pid":12106,"name":"Nikon D5200","cost":312000,"brand":"nikon","category":"camera","rating":5,"discount":40},
    {"pid":12107,"name":"Canon D10","cost":142000,"brand":"canon","category":"camera","rating":5,"discount":10},
    {"pid":12108,"name":"Sony LED TV","cost":112000,"brand":"sony","category":"tv","rating":5,"discount":10}
]

myip=int(input("Enter choice :"))
# 1 sorty by cost L2H
# 2 sort by cost H2L
# 3 sort by rating (H2L)
# 4 sort by disc (L2H)
# 5 sort by disc (H2L)
if myip<=0 or myip>5:
    print("Error in input")
    exit(-1)
myprodlist.sort(key=(lambda e1: e1["cost" if myip<=2 else "rating" if myip ==3 else "discount"]),reverse=True if myip == 2 or myip == 3 or myip == 5 else False)

for k in myprodlist:
    print(k)