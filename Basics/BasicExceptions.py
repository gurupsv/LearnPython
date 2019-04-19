
try:
    result=10+'10'
except TypeError:
    print("Blah Blah Blah!")
except OSError:
    print("OS Error")
else:
    print("In else BLOCK!!")
    print(result)
finally:
    print("In Finally Block!!")


