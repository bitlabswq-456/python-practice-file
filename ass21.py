#1.  Program for Adding, removing elements in the list.

list1 = [12,34,"harika","bhavana",57,1234,98,76,43]
list2 = list((1,2,3,4,5,6))
newlist = list1+list2
print(newlist)
list1.remove("harika")
print(list1)
list1.remove(12)
print(list1)
list2.remove(4)
print(list2)
list2.remove(6)
print(list2)
