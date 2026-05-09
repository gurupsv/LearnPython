def find_two_largest(arr):
    if len(arr) < 2:
        return None, None

    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num

    if second == float('-inf'):
        return first, None
    return first, second

if __name__ == "__main__":
    myarray = [8, 4, 5, 1, 9, 9, 3, 4, 6, 2, 3, 7, 10]
    first, second = find_two_largest(myarray)
    print(f"Array: {myarray}")
    print(f"First largest: {first}")
    print(f"Second largest: {second}")

    mystring = "This is testinG in Python"
    print(f"String slice [4:1:-1]: {mystring[4:1:-1]}")
    print(f"Count of 'i': {mystring.count('i')}")
