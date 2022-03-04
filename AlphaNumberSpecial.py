
# Write a python program to input any character and check whether it is alphabet, digit or special character.

ch=input("Enter any Number,charecter,special charecter here to check it")

if(ch>='a' and ch<='z') or (ch>='A' and ch<='Z'):
    print("Entered Number is a from of Alphabet")
elif(ch>='0' and ch<='9'):
    print("Entered Number is a form of Number")   
else:
    print("Entered Number is a form of Special Charecter")
    
