a = ("apple", "Cherry", "Banana", "Kiwi", "Strawberry")

#with for loop
for i in a:
    print(i)
print("*"*50)

#along with range and length in for loop
for i in range(len(a)):
    print(a[i])
print("*"*50)

#with while loop
i=0
while i<len(a):
    print(a[i])
    i+=1
print("*"*50)

#short-hand for loop
[print(i) for i in a]
