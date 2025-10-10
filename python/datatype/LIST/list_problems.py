p=["Hulk","Captain America","Iron Man","Thor","Black Widow"]

#Write a program to swap first and fifth element
p[0],p[4]=p[4],p[0]

print(p)
"""
#Output:
['Black Widow', 'Captain America', 'Iron Man', 'Thor', 'Hulk']
"""

#write a program to add element at second position

p.insert(1,"Spider man")
print(p)
"""
#Output:
['Black Widow', 'Spider man', 'Captain America', 'Iron Man', 'Thor', 'Hulk']
"""
#Write a program to delete element from fifth position.

p.pop(4)
print(p)

"""
#Output:
['Black Widow', 'Spider man', 'Captain America', 'Iron Man', 'Hulk']
"""
#Write a program to multiply all elements in the list with other

h=[2,37,4,18]
multi = 1
for i in h:
    multi *= i
print("Multiplication all numbers inside the list is=",multi)
"""
#OUTPUT:
Multiplication all numbers inside the list is= 5328
"""
#Write a program to get the largest AND smallest program from the list.

c=[25,89,264,45,36,75,10]
c.sort()
print("The largest value in the given list:", max(c))
print("The smallest value in the given list:", min(c))


"""
#OUTPUT:
The largest value in the given list:- 264
The smallest value in the given list:- 10
"""