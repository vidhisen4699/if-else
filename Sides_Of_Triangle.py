# Que: accept three sides of a triangle and check whether it is an equilateral, isosceles or scalence triangle
# Meaning =>
# Note :
#        An "equilateral triangle" is a triangle in which all three sides are equal.
#        A "scalene triangle" is a triangle that has three unequal sides.
#        An "isosceles triangle" is a triangle with (at least) two equal sides.



print("Input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x == y == z:
	print("Equilateral triangle")
elif x==y or y==z or z==x:
	print("Isosceles triangle")
else:
	print("Scalene triangle")