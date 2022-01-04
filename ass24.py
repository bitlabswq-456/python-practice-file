#4. Program to find the differences of two lists.
list1 = [5, 11, 30, 24, 35, 40]
list2 = [10, 80, 30, 70, 50, 66]

difference1 = set(list1).difference(set(list2))
difference2 = set(list2).difference(set(list1))

listdifference = list(difference1.union(difference2))
print(listdifference)
