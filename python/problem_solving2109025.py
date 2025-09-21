

A="Why fit in, When you are Born to Stand Out!"



#Write a program to find the length of the A="Why fit in, When you are Born to Stand Out!"
print("*"*50)
print("Length of given string is:",len(A))

"""len not only count letters in string but also count spaces between letters"""


#Write a program to check how many times alphabet "o"
# is occurring in A="Why fit in, When you are Born to Stand Out!"

print("*"*50)

print("The number of time 'o' is occurring is:",A.count("o"))
"""  capital 'O' is not counted because python is case sensitive language """



#Write a program to convert the whole given string into lower and upper cases.

print("*"*50)
print("String in lower case is as:",A.lower())

print("String in upper case is as:",A.upper())

#Write a program to convert the following string into a title

print("*"*50)
print(A.title())

#Write a program to find the index number of "fit in"
print("*"*50)
print("Method 1")
print(A.find("fit in"))
print("Method 2")
print(A.index("fit in"))
print("*"*50)

