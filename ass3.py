#3. Write a Python program to read a number n from the user and compute n+nn+nnn
#Example: If the n = 5
#5+55+555 = 615

#Input:
#Enter a number n: 20
#Output:
#The value is: 204060


n = input("Enter a number: ")
n1 = int(f"{n}")
n2 = int(f"{n}{n}")
n3 = int(f"{n}{n}{n}")
n4 = n1+n2+n3
 
print(n1)
print(n2)
print(n3)
print(f"Computed value of {n1}+{n2}+{n3} = {n4} ")

