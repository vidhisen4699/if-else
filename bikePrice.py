# Q). Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria :
    
#         Cost price (in Rs)                Tax
#         > 100000                           15 %
#         > 50000 and <= 100000              10%
#         <= 50000                           5%

tax=0
bike=int(input("Enter Number"))

if bike>=100000:
 tax=15/100*bike

elif bike > 50000 and bike <= 100000:
 tax=10/100*bike

else:
    tax=5/100*bike
    print("Tax to be paid ",tax)  