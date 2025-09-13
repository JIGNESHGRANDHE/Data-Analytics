marks = int(input("Enter your marks: "))

if marks >= 75:
    print("Grade: A")

if marks < 75 and marks >= 40:
    print("Grade: B")

if marks < 40 and marks >= 30:
    print("Grade: C")

if marks < 30:
    print("Fail")



"""
#OUTPUT:
Enter your marks: 15
Fail
"""

"""
Enter your marks: 81
Grade: A
"""
