
def sumofall(n):
    if n == 1 :
        return 1
    else :
        return sumofall(n-1)+n

print(sumofall(5))
print(sumofall(2))

word_list = ['cat','dog','rabbit']
letter_set = set()
letter_list=[]
for a_word in word_list:
    for a_letter in a_word:
        if a_letter in letter_list:
            continue
        else :
            letter_list.append(a_letter)
        letter_set.update(a_letter)
print(list(letter_set))
print(letter_list)


def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')
list2 = extendList(143,list2)

print("list1 = %s" % list1)
print("list2 = %s" % list2)
print("list3 = %s" % list3)