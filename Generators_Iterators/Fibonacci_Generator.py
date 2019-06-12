def fibonacci_generator(n):
    count, prev, current=0,0,1
    while True:
        if count == n:
            break
        else:
            yield current
            prev, current = current, current+prev
            count+=1


for i in fibonacci_generator(10):
    print(i)

