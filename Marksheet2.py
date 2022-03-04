# Accept the pecentage from the user and display the grade according to the following criteria:
# .........Below 25--D
#..........25 to 45--C
#..........45 to 50--B
#..........50 to 60--B+
#..........60 to 80--A
#....Above.80 to A+

name=str(input("Enter Student Name"))
rool_no=int(input("Enter Student Roll Number"))
Hindi_marks=int(input("Enter Hindi Marks"))
English_marks=int(input("Enter English marks"))
Maths_marks=int(input("Enter Maths Marks"))
Social_Science_marks=int(input("Enter Social Science Marks"))
Science_marks=int(input("Enter Science Marks"))
Sanskrit_marks=int(input("Enter Sanskrit Marks"))
Practical_marks=int(input("Enter Practical Marks"))




total=Hindi_marks+English_marks+Maths_marks+Social_Science_marks+Science_marks+Sanskrit_marks+Practical_marks

print("====================================================================")
print("************************Student MarkSheet***************************")
print("====================================================================")

print("Student Name:",name)
print("Student Roll Number:",rool_no)

print("====================================================================")

print("Total marks:",total)
per=total/7
print("Percentage is:",per)

print("====================================================================")

if(per>80):
    print(f"{name} is pass from A+ grade")
elif(60>per or per<=80):
    print(f"{name} is pass from A grade")
elif(50>per or per<=60):
    print(f"{name} is pass from B+ grade")
elif(45>per or per<=50):
    print(f"{name} is pass from B grade")
elif(25>per or per<=45):
    print(f"{name} is pass from C grade")
elif(per<=25):
    print(f"{name} is pass from D grade")
else:
    print(f"{name}You're fail")

print("====================================================================")