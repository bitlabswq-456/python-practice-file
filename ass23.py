#3. Program to create two lists with EVEN numbers and ODD numbers from a list. 
list1 = [10, 23, 34, 46, 57]

listOdd = []
listEven = []

for num in list1:
	if num%2 == 0:
		listEven.append(num)
	else:
		listOdd.append(num) 
print("Even numbers list:",listEven)
print("Odd numbers list:",listOdd)