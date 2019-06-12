def seperate_names(my_full_names):
    for full_name in my_full_names:
        for name in full_name.split():
            yield name


full_names = (fullname.strip() for fullname in open("names.txt"))
#names = (name.split()[1] for name in full_names)
names = seperate_names(full_names)
lengths = ((name,len(name)) for name in names)
print(max(lengths,key=lambda x:x[1]))

