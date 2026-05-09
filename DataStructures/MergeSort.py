def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1

if __name__ == "__main__":
    try:
        line = input()
        if line:
            mydata = line.split()
            if len(mydata) >= 3:
                mylist = list(mydata[0])
                start = int(mydata[1])
                end = int(mydata[2])
                tosort = mylist[start:end+1]
                mergeSort(tosort)
                mylist[start:end+1] = tosort
                print(''.join(mylist))
    except EOFError:
        pass
