"""
#Write a program to display following pattern.
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
for i in range (1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()



"""
#write a program to display following pattern.
1 1 1 1 1
2 2 2 2
3 3 3 
4 4
5
"""
print("\n")
print("*"*50)
for i in range(1,6):
    for j in range(6,i,-1):
        print(i,end=" ")
    print()



"""
#write a program to display following pattern.
        1 
      1 2 
    1 2 3 
  1 2 3 4 
1 2 3 4 5 
"""
print("\n")
print("*"*50)
for i in range(1,6):
    for j in range(5,i,-1):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(k,end=" ")
    print()



"""
#write a program to display following pattern.
1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1 
6 5 4 3 2 1 
7 6 5 4 3 2 1 
8 7 6 5 4 3 2 1 
9 8 7 6 5 4 3 2 1 
"""
print("\n")
print("*"*50)
for i in range(1,10):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()



"""
#write a program to display following pattern.
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
"""
print("\n")
print("*"*50)
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(1,5):
    for j in range(5,i,-1):
        print("*",end=" ")
    print()

print("\n")
print("*"*50)


"""
#write a program to display following pattern.
1 
2 4 
3 6 9 
4 8 12 16 
5 10 15 20 25 
6 12 18 24 30 36 
7 14 21 28 35 42 49 
8 16 24 32 40 48 56 64 
9 18 27 36 45 54 63 72 81 
10 20 30 40 50 60 70 80 90 100 
"""
for i in range(1,11):
    for j in range(1,i+1):
        print(i*j,end=" ")
    print()


