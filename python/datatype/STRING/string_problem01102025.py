#Write a program to separate the following string
# into comma separated values
a="OOTD.YOLO.ASAP.BRB.GTG.OTW"
print(a.split("."))
"""
#OUTPUT
['OOTD', 'YOLO', 'ASAP', 'BRB', 'GTG', 'OTW']
"""

#Write a program to sort strings alphabetically.
print("*"*50)
s=input("enter a string:-")
print(sorted(s))
"""
#OUTPUT
enter a string:-Zebra in the zoo
[' ', ' ', ' ', 'Z', 'a', 'b', 'e', 'e', 'h', 'i', 'n', 'o', 'o', 'r', 't', 'z']
"""

#Write a program to replace a given character from a string.
print("*"*50)
h="Python programming"
print(h.replace("Python","Java"))   #Java programming
x="P..Y...T.H.O.N..."
print(x.replace(".",""))            #PYTHON



#Write a program to check the number of occurrence of a
#substring in string
print("*"*50)
p=input("enter a string:-")
p1=input("enter a substring:-")
p3=(p.count(p1))
print("The",p1,"is occurring",p3,"times in",p)

"""
#OUTPUT
enter a string:-She sells seashells on the sea shore
enter a substring:-sh
The sh is occurring 2 times in She sells seashells on the sea shore
"""

