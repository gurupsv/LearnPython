file=open("demo.txt","r")
lines=file.readlines()
for line in lines[2:5]:
    print(line)
file.close()