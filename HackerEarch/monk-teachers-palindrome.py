'''
Problem link : https://www.hackerearth.com/practice/algorithms/string-algorithm/basics-of-string-manipulation/practice-problems/algorithm/monk-teaches-palindrome/

Input :-
3
abc
abba
aba

O/P :-
NO
YES EVEN
YEs ODD
'''
mycount=int(input())
for i in range(mycount):
    mystring = input()
    mylen = len(mystring)
    palendrome=True
    for i in range(mylen//2):
        if mystring[i] != mystring[mylen-1-i] :
            palendrome=False
            break

    if palendrome :
        print('YES', 'ODD' if mylen%2 else 'EVEN')
    else:
        print('NO')
