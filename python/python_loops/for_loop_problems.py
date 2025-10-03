#write a program for Fibonacci Series
num=int(input("Enter a number:"))
a=0
b=1
print(a)
print(b)
for i in range(2,num):
    c=a+b
    a=b
    b=c
    print(c)
#write a program for identify the number is prime or not
NUM=int(input("Enter a number:"))
if NUM<=1:
    print("It is not a prime number")
else:
    for i in range(2,NUM):
        if NUM%i==0:
            print("It is not prime number")
            break
    else:
        print("It is a prime number")
#Write a program to find the integer is palindrome or not
num=int(input("Enter a number:"))
temp=num
rev=0
while num>0:
    dig=num%10
    rev=rev*10+dig
    num=num//10
if rev == temp:
    print("It is palindrome.")
else:
    print("It is not palindrome.")