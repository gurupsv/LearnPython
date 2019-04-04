
# testcount = int(input())
#
# for tst in range(testcount):
#     mydata = input().split()
#     mylist = list(mydata[0])
#     #mylist.sort()
#     for i in range(int(mydata[2]), int(mydata[1]), -1):
#         for j in range(int(mydata[1]),i):
#             if mylist[j] < mylist[j+1]:
#                 temp=mylist[j]
#                 mylist[j]=mylist[j+1]
#                 mylist[j+1]=temp
#     print(''.join(mylist))


testcount = int(input())

def partition(xs, start, end):
    follower = leader = start
    while leader < end:
        if xs[leader] > xs[end]:
            xs[follower], xs[leader] = xs[leader], xs[follower]
            follower += 1
        leader += 1
    xs[follower], xs[end] = xs[end], xs[follower]
    return follower


def _quicksort(xs, start, end):
    if start >= end:
        return
    p = partition(xs, start, end)
    _quicksort(xs, start, p-1)
    _quicksort(xs, p+1, end)


for tst in range(testcount):
    mydata = input().split()
    mylist = list(mydata[0])
    _quicksort(mylist, int(mydata[1]), int(mydata[2]))
    print(''.join(mylist))