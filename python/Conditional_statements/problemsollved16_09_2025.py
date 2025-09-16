# Write a program to check number is positive or not
num = int(input("Enter a number= "))
print("entered number=", num)

if num >= 0:
    print("number is positive ")
else:
    print("number is negative ")

"""
# SAMPLE OUTPUT:
Enter a number= 23
entered number= 23
number is positive 

Enter a number= -12
entered number= -12
number is negative 
"""

# Write a program to check a number is odd or even
numb = int(input("Enter a number= "))

if numb % 2 == 0:
    print("number is even")
else:
    print("number is odd")

"""
# SAMPLE OUTPUT:
Enter a number= 1
number is odd

Enter a number= 2
number is even
"""

# Write a program to create area calculator
print("*******AREA calculator*********")
print("""
press 1 for area of square
press 2 for area of rectangle
press 3 for area of circle
press 4 for area of triangle""")

choice = int(input("Enter a number from 1 to 4:"))
if choice == 1:
    side = float(input("Enter side of square:"))
    areasq = side**2
    print("The area of square is=", areasq)
elif choice == 2:
    length = float(input("Enter length of rectangle:"))
    width = float(input("Enter breadth of rectangle:"))
    arearec = length * width
    print("The area of rectangle is=", arearec)
elif choice == 3:
    radius = float(input("Enter radius of circle:"))
    areacircle = ((22 / 7) * (radius**2))
    print("The area of circle is=", areacircle)
elif choice == 4:
    base = float(input("Enter base:"))
    height = float(input("Enter height:"))
    areatriangle = 0.5 * base * height
    print("The area of triangle is=", areatriangle)
else:
    print("Invalid input")

"""
# SAMPLE OUTPUTS:

Case 1: Square
*******AREA calculator*********
press 1 for area of square
press 2 for area of rectangle
press 3 for area of circle
press 4 for area of triangle
Enter a number from 1 to 4:1
Enter side of square:5
The area of square is= 25.0

Case 2: Rectangle
Enter a number from 1 to 4:2
Enter length of rectangle:2.5
Enter breadth of rectangle:0.62
The area of rectangle is= 1.55

Case 3: Circle
Enter a number from 1 to 4:3
Enter radius of circle:7
The area of circle is= 154.0

Case 4: Triangle
Enter a number from 1 to 4:4
Enter base:10
Enter height:5
The area of triangle is= 25.0

Case 5: Invalid
Enter a number from 1 to 4:6
Invalid input
"""

# Write a program to identify the number is single, double, triple, four, or five digit
num = int(input("Enter a number="))
if num >= 0 and num <= 9:
    print("the number is single digit")
elif num >= 10 and num <= 99:
    print("the number is double digit")
elif num >= 100 and num <= 999:
    print("the number is triple digit")
elif num >= 1000 and num <= 9999:
    print("the number is four digit")
else:
    print("number is five digit")

"""
# SAMPLE OUTPUTS:
Enter a number=5
the number is single digit

Enter a number=42
the number is double digit

Enter a number=325
the number is triple digit

Enter a number=7564
the number is four digit

Enter a number=12345
number is five digit
"""
