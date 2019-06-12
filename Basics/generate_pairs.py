def generate_pairs(array,x):
    myset={z for z in array}
    while len(myset):
        i=myset.pop()
        for j in myset:
            if (i+j==8):
                print(i,",",j)
                continue
    

def get_missing(array):
    length=len(array)
    for i in range(1,length+1):
        found=False
        for j in array:
            if i==j:
                found=True
                continue
        if found != True :
            print(i)
            break

myarray=[1,3,5,8,2,0,4,4,-1,9,10,-2]

#generate_pairs(myarray, 8)
get_missing(myarray)
get_missing([1,2,3,4,7,8,5,6,10])
