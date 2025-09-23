# write a program to find sum of all even numbers upto fifty
sum=0
for i in range (0,51):
    if i%2==0:

        sum=sum+i
print("The sum of first even numbers upto fifty is",sum)


"""
#OUTPUT
The sum of first even numbers upto fifty is 650
"""


# write a program for first 20 numbers  and their squared numbers
print("\n")
for i in range(1,21):
    print(i,"=",i*i)

"""
1 = 1
2 = 4
3 = 9
4 = 16
5 = 25
6 = 36
7 = 49
8 = 64
9 = 81
10 = 100
11 = 121
12 = 144
13 = 169
14 = 196
15 = 225
16 = 256
17 = 289
18 = 324
19 = 361
20 = 400
"""


# write a program to find sum of first 10 odd numbers using while loop
print("\n")
n=0
sum=0
while n<=20  :
    if n%2!=0:
        sum = sum + n
    n = n+1
print(sum)

"""
#OUTPUT
100
"""


#write a program to create a basic billing system at supermarket from cashier perspective
print("\n")
while True:
    name = input("\nenter customer name=")
    total=0
    while True:
        item_name = input("enter item name=")
        print("enter the amount and Quantity")
        amount=float(input("Enter the rate of item="))
        quantity=float(input("Enter the Quantity of item="))
        total+=quantity*amount
        print(total)
        repeat= input("Do you want to add more items?(y/n)")
        if repeat=="n" or repeat=="N":
            break
    print("*"*50)
    print("customer name=",name)
    print("total amount to be paid=",total,"Rs")
    print("*" * 50)
    print("")


    repeat1=input("Do you want to go next customer ?(y/n)")
    if repeat1 == "n" or repeat1 == "N":
        break


"""
#OUTPUT
enter customer name= Harshal
enter item name=sugar
enter the amount and Quantity
Enter the rate of item=40
Enter the Quantity of item=2
80.0
Do you want to add more items?(y/n)y
enter item name=wheat flour
enter the amount and Quantity
Enter the rate of item=50
Enter the Quantity of item=1.5
155.0
Do you want to add more items?(y/n)y
enter item name=jelly
enter the amount and Quantity
Enter the rate of item=10
Enter the Quantity of item=5
205.0
Do you want to add more items?(y/n)n
**************************************************
customer name=  Harshal
total amount to be paid= 205.0 Rs
**************************************************

Do you want to go next customer ?(y/n)y

enter customer name=Aditya
enter item name=tyre
enter the amount and Quantity
Enter the rate of item=1000
Enter the Quantity of item=2
2000.0
Do you want to add more items?(y/n)y
enter item name=bearings
enter the amount and Quantity
Enter the rate of item=18
Enter the Quantity of item=6
2108.0
Do you want to add more items?(y/n)n
**************************************************
customer name= Aditya
total amount to be paid= 2108.0 Rs
**************************************************

Do you want to go next customer ?(y/n)n
"""
