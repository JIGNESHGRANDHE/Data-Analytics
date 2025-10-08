
a=["Dog","Cat","horse","Goat","cow","cat"]
print(a)

#Write a program to create a copy of list
b=[]
print(b)
b=a.copy()
print(b)

#write a program to get the index number
print(a.index("Dog"))
print(a.index("Cat"))
print(a.index("cat"))


#write a program to extend the list
v=["rabbit","Duck"]
a.extend(v)
print(a)

#write a program to reverse the list
a.reverse()
print(a)

#Write a program to sort a list
a.sort()
print(a)


d=[1.26,45,896,1000,0.25,3.14]
d.sort()
print(d)



#write a program to clear the data from the list

k=[1.26,45,896,1000,0.25,3.14,"Dog","Cat","horse","Goat","cow","cat"]
k.clear()

print(k)