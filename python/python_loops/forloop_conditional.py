#for loop with conditional statement
for i in range(1,10):
    if i==3:
        print("good work")
    else:
        print(i)


"""
#OUTPUT
1
2
good work
4
5
6
7
8
9
"""

#program for getting the numbers which are divisible by any two numbers, in entered range by user
while True:
    divisor1=int(input("Enter first divisor:"))
    divisor2=int(input("Enter second divisor:"))
    start_range=int(input("Enter range starting number:"))
    end_range=int(input("Enter range ending number (ensure it is greater than one place):"))
    for i in range(start_range,end_range):
        if i%divisor1==0 and i%divisor2==0:
            print(i)
    repeat_a=(input("you want to check for other numbers or range type:-(y/n)"))
    if repeat_a=="n" or repeat_a=="N":
        break

"""
#OUTPUT
Enter first divisor:1
Enter second divisor:2
Enter range starting number:1
Enter range ending number (ensure it is greater than one place):9
2
4
6
8
you want to check for other numbers or range type:-(y/n)y
Enter first divisor:1
Enter second divisor:2
Enter range starting number:20
Enter range ending number (ensure it is greater than one place):39
20
22
24
26
28
30
32
34
36
38
you want to check for other numbers or range type:-(y/n)n
"""