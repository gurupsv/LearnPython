# URL :- https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/help-jarvis-8a39566e/

no_trains = int(input())
for i in range(no_trains):
    mynum = int(input())
    count=0
    for i in range(1, 8):
        if mynum > 10**(i-1):
            if str(mynum).__contains__(str(i)):
                count += 1
        else:
            break
    if count == i-1:
        print("YES")
    else:
        print("NO")
