
while True:
    print("\n*******AREA calculator*********")
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
    repeat = input("do you want to repeat? (y/n)")

    if repeat == "n" or repeat == "N":
        break

"""
CASE 1:-
*******A0REA calculator*********

    press 1 for area of square
    press 2 for area of rectangle
    press 3 for area of circle
    press 4 for area of triangle
Enter a number from 1 to 4:5
Invalid input
do you want to repeat? (y/n)



CASE 2:-
*******AREA calculator*********

    press 1 for area of square
    press 2 for area of rectangle
    press 3 for area of circle
    press 4 for area of triangle
Enter a number from 1 to 4:1
Enter side of square:5
The area of square is= 25.0
do you want to repeat? (y/n)N


CASE 3:-

*******AREA calculator*********

    press 1 for area of square
    press 2 for area of rectangle
    press 3 for area of circle
    press 4 for area of triangle
Enter a number from 1 to 4:2
Enter length of rectangle:6
Enter breadth of rectangle:6.1
The area of rectangle is= 36.599999999999994
do you want to repeat? (y/n)Y

*******AREA calculator*********

    press 1 for area of square
    press 2 for area of rectangle
    press 3 for area of circle
    press 4 for area of triangle
Enter a number from 1 to 4:
"""
