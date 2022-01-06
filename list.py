#find sum and average of a list elements

l =[]

n=int(input("enter number"))

for i in range(0,n):

    val=int(input("enter number"))

    l.append(val)

print(l)

count=0

for i in l:

    count=count+i

print("sum:", count)

avg=count//len(l)

print("average:",avg)