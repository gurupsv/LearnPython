def switchCase(ltr):
    if ltr.islower():
        return ltr.upper()
    elif ltr.isupper():
        return ltr.lower()
    else :
        return ltr




mystring="This is 2 PyThOnIc.."
cstr=str().join([switchCase(x) for x in mystring])
print(cstr)