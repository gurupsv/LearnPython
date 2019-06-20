# m=input()
# c,l=0,0
# for i in m:
#     if i in 'aeiou':
#         c+=1
#         l=c if c>l else l
#     else:
#         c=0
# print(l)

import re
a=input()
b=re.findall(r'[aeiou]+',a)
c=0
for i in b:
    j=len(i)
    c=j if c<j else c
print(c)