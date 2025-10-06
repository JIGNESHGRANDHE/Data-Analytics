#Iteration of List using For Loop
o=["Cricket","Football","Tennis","Golf"]
for m in o:
    print(m)


#Iteration using For Loop with Range and Length function
for i in range(len(o)):
    print(i)


#Iteration using While Loop
print("*"*50)
i=0
while i<len(o):
    print(o[i])
    i += 1


#Iteration using Short hand For Loop
print("*"*50)
[print (i) for i in o]