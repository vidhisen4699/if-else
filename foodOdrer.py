# program to take food order from user through a simple python program.

a=int(input('''Enter 1 for Burger
              Enter 2 for Pizza 
              Enter 3 for Noodles
              Enter 4 for Manchurian'''))
if a==1:
    print('Your Burger will be delivered in 5 minutes')
elif a==2:
    print('Your Pizza will be delivered in 5 minutes')
elif a==3:
    print('Your Noodles will be delivered in 5 minutes')
elif a==4:
    print('Your Manchurian will be delivered in 5 minutes')
else:
    print('Enter Correct Order Number')