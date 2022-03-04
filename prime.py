# Using If Condition
num=int(input('Enter number'))

if num%1==0 and num%2!=0 and num%num==0:
    print('It is Prime Number')
else:
    print('It is Not Prime Number')    


'''
# Using Loop
num=int(input("Enter Number"))

count=0
i=1
while(i<=num):
    if (num%i==0):
        count=count+1
    i=i+1
if(count==2):
    print("prime")
else:     
    print("Not Prime")        
'''

# if num%2!=0 and num%3!=0 and num%5!=0 and num%7!=0 or num==2 and num==3 and num==5 and num==7:
#     print(num,"not prime")
# else :
#     print(" prime")
# if num>1:
#  #   for i in range(2,num):
#         i=2
#         if(num%i)==0:
#             print(num,"is not prime Number")
#          #   break
#         else:
#             print(num,"is a prime Number")


