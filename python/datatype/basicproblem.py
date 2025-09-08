print("""write  a program to display a person's name,age and
 address in different lines.""")

name=input("enter your name:")
age=int(input("enter your age:"))
address=input("enter your address:")
print("Name=",name)
print("Age=",age)
print("Address=",address)

#output
"""enter your name:Jignesh
enter your age:21
enter your address:SB road 375
Name:Jignesh
Age:21
Address:SB road 375"""

print("""write a program to swap to numbers 
method 1 to swap two numbers""")
x=23
y=45
print("initial x=",x," initial y=",y)
temp=x
print("temp=",temp)
x=y
print("x=",x)
y=temp
print("after swapping y=",y)
print("after swapping x=",x)


"""initial x= 23  initial y= 45
temp= 23
x= 45
after swapping y= 23
after swapping x= 45"""


print("""method 2 to swap two numbers""")
x=int(input("enter number="))
y=int(input("enter number="))
print("initial x=",x," initial y=",y)
x,y=y,x
print("after swapping x=",x)
print("after swapping y=",y)
#OUTPUT
"""
enter number=12
enter number=23
initial x= 12  initial y= 23
after swapping x= 23
after swapping y= 12
"""

print("""Write a program to convert float into integer""")

a=float(input("enter number="))
print(a)
print(type(a))
a=int(a)
print(a)
print(type(a))
#OUTPUT
"""
enter number=15.4
15.4
<class 'float'>
15
<class 'int'>
"""


print("""write a program to take details from a student fot
 ID card and then print it in different lines""")


name = input("enter your name:")
age = int(input("enter your age:"))
grade = int(input("enter your grade:"))
email = input("enter your email:")
ph_no=input("enter your phone number:")
print("Student Identity Card")
print("Name=",name)
print("Age=",age)
print("Grade=",grade)
print("Email=",email)
print("Phone Number=",ph_no)
#OUTPUT
"""
enter your name:Jignesh
enter your age:10
enter your grade:5
enter your email:jignesh@gmail.com
enter your phone number:8669079910
Student Identity Card
Name= Jignesh
Age= 10
Grade= 5
Email= jignesh@gmail.com
Phone Number= 8669079910
"""


print("""write a program to convert integer into float""")
a=int(input("enter number="))
print(a)
print(type(a))
a=float(a)
print(a)
print(type(a))
#OUTPUT
"""
enter number=15
15
<class 'int'>
15.0
<class 'float'>
"""
