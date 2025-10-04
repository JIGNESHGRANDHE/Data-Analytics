#take an input from user as a string then, reverse it
s1=input("enter a string:-")
print("Reverse of string=",s1[::-1])
"""
#OUTPUT
enter a string:-Onion
Reverse of string= noinO

"""

# write a program to check if the string contains only digit
print("*"*40)
s2=input("enter anything here:-")
s22=(s2.isdigit())
if s22==True:
    print(s2,"contains only Digit.")
else:
    print(s2,"does not contain only Digits.")
"""
#OUTPUT
case->1
enter anything here:-586
586 contain only Digit.
case->2
enter anything here:-oik56
oik56 does not contain only Digits.
"""
#check the entered number or string is palindrome or not
print("*"*40)
p=(input("enter the number/word:-"))
c=(p[::-1])
if p==c:
    print(p,"is palindrome")
else:
    print(p,"is not palindrome")
"""
#OUTPUT
case->1
enter the number/word:-racecar
racecar is palindrome
case->2
enter the number/word:-785
785 is not palindrome
"""
#Write a program to find the number of vowels in the string
print("*"*40)
l=input("enter anything here:-")
vowels=0
for i in l:
    if i in "aeiouAEIOU":
        vowels+=1
print("total number of vowels in *",l,"* is",vowels)
"""
#OUTPUT
enter anything here:-Fourteen is bigger than twelve
total number of vowels in * Fourteen is bigger than twelve * is 10
"""
#write a program to check if every word in a string begins with a capital letter.
print("*"*40)
a=input("enter a string:-")
print(a.istitle())

"""
#OUTPUT
case->1
enter a string:-Man Vs Wild
True
case->2
enter a string:-Man vs Wild
False
"""