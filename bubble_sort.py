
array=[4,2,6,8,3,1,9,5,7]
print ("Original Array : ", array)

def bubblesort(array):
    for i in range(len(array)-1,0,-1):
        print ("After Round",i," : ", array)
        for j in range(i):
            if array[j] > array[j+1]:
                temp=array[j]
                array[j]=array[j+1]
                array[j+1]=temp

bubblesort(array)
print ("Sorted Array : ", array)