#Task 4
# problem 1
# to find even numbers and odd numbers from the given list

"""Logic:
1)Declare a list
2)Declare 2 empty list for odd and even numbers.
3)using conditional statement check
if the number is even or odd.
4)If the number is even, append it to the even list.
If the number is odd, append it to the odd list."""

print("Problem 1 :")
# creating a list of numbers
lst=[10,501,22,37,100,999,87,351]
# Display the list
print("To find even and odd numbers from the list:", lst)
# Declare two empty lists for even and odd numbers
even_numbers = []
odd_numbers = []

# Loop through the list and check if each number is even or odd
for number in lst:
    # Check if the number is even and append it to even list
    if number % 2 == 0:
        even_numbers.append(number)
    # If the number is odd, append it to odd list
    else:
        odd_numbers.append(number)

# Display the even and odd numbers
print("Even numbers:", even_numbers)
print("Odd numbers:",odd_numbers)
print('\n')


#problem 2
# To find prime numbers from the given list

# """Logic:
# 1)Declare a list
# 2)Declare an empty list for prime numbers.
# 3)Loop through the list and check if each number is prime.
# 4)If the number is prime, append it to the prime list.
#  5)Count the total number of prime numbers and display it."""

print("Problem 2 :")
# Creating a list of numbers
lst = [10, 501, 22, 37, 100, 999, 87, 351]
# declare an empty list for prime numbers and print the list
prime_numbers=[]
print('finding the prime numbers and count of prime numbers from the given list:',lst)

# Loop through the list to check for prime numbers
# Prime numbers are numbers that are divisible by 1 and itself,so we start checking from 2
for i in lst:
    for j in range(2,i):
        # If the number is divisible by any number other than 1 and itself, it is not prime
        # So we break the loop and move to the next number
        if i % j == 0:
            # non_prime.append(i)
            break
    # If the loop completes without breaking, the number is prime
    else:
        prime_numbers.append(i)

# Count of prime numbers
PRIME_COUNT = len(prime_numbers)
# Display the prime numbers and their count
print("Prime numbers:", prime_numbers)
print("Total prime numbers:", PRIME_COUNT)
print('\n')


#problem 3
# To find happy numbers from the given list

# """Logic:
# 1)Declare a list
# 2)Declare an empty list for happy numbers.
# 3)Loop through the list and check if each number is happy.
# 4)If the number is happy, append it to the happy list
# 5)Display the happy numbers."""

print("Problem 3 :")
# Creating a list of numbers
lst = [10, 501, 22, 37, 100, 999, 87, 351]
# Declare an empty list for happy numbers and print the list
print("To find happy numbers from the list:", lst)
happy_numbers = []

# Loop through the list to check for happy numbers
# 1. Starting with the number, replace the number by the sum of the squares of its digits.
# 2. Repeat the process until the number is less than 10.
for num in lst:
    # Initialize i with the current number
    i=num
    # Initialize s to 0 for sum of squares of digits
    while i>=10:
        S=0
      # Sum of squares of digits
        while i >0:
            DIGIT = i % 10
            #print(digit)
            S= S+ (DIGIT * DIGIT)
            #print(sum)
            i = i // 10
            #print(i)
        i=S
        #print("sum=",i)
    # If the final result is 1, the number is happy and append it to the happy list
    if i == 1:
        happy_numbers.append(num)

# Display the happy numbers
print("happy numbers are:", happy_numbers)
print('\n')


#Problem 4
# sum to add first and last digits
# To find the sum of the first and last digit of a number
# """Logic:
# 1)Take a number as input.
# 2)Find the last digit using modulus operator.
# 3)Use a loop to find the first digit by continuously dividing the number by 10.
# 4)Add the first and last digit and display the result."""

print("Problem 4 : to find sum of first & last digit of a number")
# Take a number as input and typecast it to integer
number=int(input("enter a number above 10:"))
DIGIT=0
num=number

# to find the last digit of the number
last_digit= number % 10

# find the first digit of the number
while number > 0:
    DIGIT = number % 10
    number = number // 10
# After the loop, digit will hold the first digit
first_digit = DIGIT
# Calculate the sum of first and last digit and display the result
sum_numbers = first_digit+last_digit

print(f"sum of first and last digit in the number {num} is:",sum_numbers )
print('\n')

#problem 5
print("Problem 5 :")
# To find the combinations of coins to form a total amount
# """Logic:
# 1)Declare a list of coins.
# 2)Declare an empty list to store combinations.
# 3)Declare a variable for the total amount.
# 4)Using loops in list and find combinations that sum up to 10
# 5)If the sum equals 10, append the combination to the combinations list.
# 6)Display the combinations."""

coins = [1,2,5,10]
combinations=[]
TOTAL=10
S=0
print(f'To find combination from coins Rs.{coins} to form rs.{TOTAL}')

# Loop to check possible counts for each coin
# and check if the sum equals 10

for i in range(0,11):
    for j in coins:
        S=j*i
        if S==10:
            combinations.append([j,i])
            print("Rs.", [j], '*', [i], '=', [j, i])
print("the combinations form Rs.10 are:",combinations)
print('\n')





#problem 6
print("Problem 6 :")
# To find duplicates in three lists
# """Logic:
# 1)Declare three lists.
# 2)Declare an empty list for duplicates.
# 3)Loop through the first list and check if each element is present in the other two lists.
# 4)If the element is present in both lists, append it to the duplicates list.
# 5)Display the duplicates."""

# Declare three lists and an empty list for duplicates
lst1=[1,8,31,18,6,22,86,91,16]
lst2=[1,5,4,8,6,31,46,88]
lst3=[1,6,8,24,31,96,81]
duplicate=[]

# Loop through the first list and check for duplicates in the other two lists
for i in lst1:
    # if the element is present in both lst2 and lst3, append it to the duplicate list
    if i in (lst2 and lst3):
        duplicate.append(i)

# Display the duplicates found in the three lists
print("To find duplicates in the three lists,")
print(f"lst1={lst1}")
print(f"lst2={lst2}")
print(f"lst3={lst3}")
print('Duplicates in the list are :',duplicate)
print('\n')

#problem 7
print("Problem 7 :")
# To find the first non-repeating number in a list
# """Logic:
# 1)Declare a list of numbers.
# 2)Loop through the list and count the occurrences of each number.
# 3)If the count is 1, print the number and break the loop.
# 4)Display the first non-repeating number."""

# Declare a list of numbers and print the list
number=[1,8,31,18,6,22,86,91,16,18,31,1,8]
COUNT=0
print(f'To find first non repeating number from the list: {number}')

# Loop through the list to find the first non-repeating number
# Using count() find the occurrences of each number
for i in number:
    j=number.count(i)
    # If the count is 1, print the number and break the loop
    if j==1:
        print("The first non repeating number is:",i)
        break
print('\n')

#problem 8
print("Problem 8 :")
# To find the minimum number from a list
# """Logic:
# 1)Declare a list of numbers.
# 2)Sort the list in ascending order.
# 3)The first element of the sorted list is the minimum number.
# 4)Display the minimum number."""

# Declare a list of numbers and print the list
lst=[31,18,6,8,1,22,86,91,16]
print(f'To find the minimum number from the list: {lst}')

# Sort the list in ascending order and print list
lst.sort()
print('sorted list:',lst)

# The first element of the sorted list is the minimum number
minimum_element=min(lst)
print('Minimum element is:',minimum_element)
# print(lst[0])
print('\n')

# Problem 9
print("Problem 9 :")

# To find triplet numbers in a list whose sum equals a given value
# """Logic:
# 1)Declare a list of numbers.
# 2)Declare a variable for the target value.
# 3)Loop through the list using three nested loops to find triplet numbers.
# 4)If the sum of the triplet numbers equals the target value, print the triplet.
# 5)Display the triplet numbers."""

# Declare a list of numbers and a target value and print it
number=[10,20,30,9]
VALUE=59
print(f"To find the Triplet number in list:{number} whose sum equal to {VALUE}")
N=len(number)

# Loop through the list using three nested loops to find triplet numbers
# If the sum of the triplet numbers equals the target value, print the triplet
for i in range(N):
    a=number[i]
    for j in range(i+1,N):
        b=number[j]
        for k in range(j+1,N):
            c=number[k]
            if a+b+c==VALUE:
                print("triplet Number whose value is equal to 59 are:",a,b,c)
print('\n')

# Problem 10
print("Problem 10 :")

# To find sublist numbers in a list whose sum equals zero
# """Logic:
# 1)Declare a list of numbers.
# 2)Loop through the list using two nested loops to find sublists.
# 3)If the sum of the sublist equals zero, print the sublist.
# 4)Display the sublist numbers."""

# create a list and print it
number=[4,2,-3,1,6]
print(f"To find the sublist from the list:{number} whose sum equal to 0")
N=len(number)

for i in range(N):
    TOTAL=0
    # Loop through the list using two nested loops to find sublists
    for j in range(i,N):
        TOTAL=TOTAL+number[j]
        # If the sum of the sublist equals zero, print the sublist
        # Display the sublist numbers
        if TOTAL==0:
            print("sublist Number whose sum is equal to 0 are:",number[i:j+1])
print('\n')
