array_count = int(input())
array_a = input().split()
array_b = input().split()

array_c = [int(array_a[i])+int(array_b[i]) for i in range(array_count)]

print(*array_c, sep=" ")

print(*(int(array_a[i])+int(array_b[i]) for i in range(array_count)))