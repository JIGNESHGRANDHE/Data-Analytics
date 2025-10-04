print("\n*******AREA calculator*********")
while True:
    print("""
    press 1 for area of square
    press 2 for area of rectangle
    press 3 for area of circle
    press 4 for area of triangle""")

    choice = int(input("Enter a number from 1 to 4:"))
    if choice==0 or choice>4:
        print("invalid input, Please enter a number from 1 to 4")
    else:
        if choice == 1:
            while True:
                side = float(input("Enter side of square:"))
                areasq = side**2
                print("The area of square is=", areasq)
                repeatsqare = input("do you want area of another square? (y/n)")
                if repeatsqare == "n" or repeatsqare == "N":
                    break
        if choice == 2:
            while True:
                length = float(input("Enter length of rectangle:"))
                width = float(input("Enter breadth of rectangle:"))
                arearec = length * width
                print("The area of rectangle is=", arearec)
                repeatrec = input("do you want area of another rectangle? (y/n)")
                if repeatrec == "n" or repeatrec == "N":
                    break
        if choice == 3:
            while True:
                radius = float(input("Enter radius of circle:"))
                areacircle = ((22 / 7) * (radius**2))
                print("The area of circle is=", areacircle)
                repeatcircle = input("do you want area of another circle? (y/n)")
                if repeatcircle == "n" or repeatcircle == "N":
                    break
        if choice == 4:
            while True:
                base = float(input("Enter base:"))
                height = float(input("Enter height:"))
                areatriangle = 0.5 * base * height
                print("The area of triangle is=", areatriangle)
                repeattriangle = input("do you want area of another triangle? (y/n)")
                if repeattriangle == "n" or repeattriangle == "N":

                    break

    repeatmenu= input("do you want repeat Menu? (y/n)")
    if repeatmenu == "n" or repeatmenu == "N":
        break
