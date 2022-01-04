#4. Write code to obtain fee amount from the user and then calculate fee hike as 10% of fees and print the newly revised amount.

#Input: 28500
#Output: 31350.0

amount = int(input('Enter Amount'))
fee_hike = 0.1*amount
total_fee = amount + fee_hike
print(total_fee)