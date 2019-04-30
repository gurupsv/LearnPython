import csv
fo= open('first.csv',"r")
reader = csv.reader(fo, delimiter=':')
print(list(reader))
#list of list