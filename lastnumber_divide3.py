# Q). Write a program to check whether the last digit of a number( entered by user ) is divisible by 3 or not.

num=int(input("Enter any number"))

ld=num%10
if ld%3==0:
     print("Last digit of number is divisible by 3 ")
else:
     print("Last digit of number is not divisible by 3 ")