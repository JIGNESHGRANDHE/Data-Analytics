
#Find maximum and minimum values in a set
print("Write a program to find max and min values in a set.")
a = {12, 56, 19, 51, 74, 86, 0, 156}

print("The minimum value in set is =", min(a)) # 0
print("The maximum value in set is =", max(a)) # 156
print("*" * 50)


#Find common elements in three lists using sets
print("Write a program to find common elements in three lists using sets.")
c = [1, 56, 2, 28, 24, 4, 5]
v = [56, 7, 112, 5, 98]
b = [1, 68, 79, 2, 5, 33, 56]

n = set(c) & set(v) & set(b)
print("The common elements in three given lists are =", n) # {56, 5}
print("*" * 50)


#Find the difference between two sets
print("Write a program to find the difference between two sets.")
c = {1, 56, 2, 28, 24, 4, 5}
v = {56, 7, 112, 5, 98}

print("Elements in c but not in v:", c.difference(v)) # {1, 2, 4, 24, 28}
print("Elements in v but not in c:", v.difference(c)) # {112, 98, 7}
print("*" * 50)


#Remove an item from a set if it is present
print("Write a program to remove an item from a set if present.")
j = {10, 2, 59, 88, 37, 18, 91}
j.discard(10)
print("After discarding 10:", j) # {2, 18, 91, 37, 88, 59}
j.discard(12)
print("After trying to discard 12 (not present):", j)  # {2, 18, 91, 37, 88, 59}
print("*" * 50)


#Check if a set is a subset of another set
print("Write a program to check if a set is a subset of another set.")
e = {1, 2, 3, 4, 5, 6, 7}
r = {5, 7, 6}

print(r.issubset(e)) # True
print("*" * 50)
