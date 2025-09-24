a="Hello"
b="Hello123"
c="123456"
d="HELLO"
e="    "
f="Hello 123@"
g="1.234"

#isalnum - Returns True if all characters in the string are alphanumeric (Alphabets and numbers )
print("\n")
print(" isalnum ".center(50,"*"))
print(a,"=",a.isalnum())  #True:-Hello is perfect string
print(b,"=",b.isalnum())  #True:-Hello123 is consist of alphabets and numbers so no issues
print(c,"=",c.isalnum())  #True:-123456 is consist of only numbers
print(d,"=",d.isalnum())  #True:-HELLO is perfect string
print(e,"=",e.isalnum())  #False:-because of space
print(f,"=",f.isalnum())  #False:-because of special char and space
print(g,"=",g.isalnum())  #False:-decimal point is there

#isalpha - Returns True if all characters in the string are in the alphabet (Only Alphabets)
print("\n")
print(" isalpha ".center(50,"*"))
print(a,"=",a.isalpha())  #True:-Hello is string with only alphabets
print(b,"=",b.isalpha())  #False:-Hello123 is string but consist of numbers
print(c,"=",c.isalpha())  #False:-123456 only numbers
print(d,"=",d.isalpha())  #True:-HELLO is string with only alphabets
print(e,"=",e.isalpha())  #False:-because of space
print(f,"=",f.isalpha())  #False:-perfect string but because of special char,space and number
print(g,"=",g.isalpha())  #False:-number and presence of point

#isdecimal - Returns True if all characters in the string are decimals (check decimal or numbers)
print("\n")
print(" isdecimal ".center(50,"*"))
print(a,"=",a.isdecimal()) #False:-only presence of characters
print(b,"=",b.isdecimal()) #False:-numbers are present but with alphabets
print(c,"=",c.isdecimal()) #True:-Only digits 0-9 (no other characters)
print(d,"=",d.isdecimal()) #False:-only presence of alphabets
print(e,"=",e.isdecimal()) #False:-space presence
print(f,"=",f.isdecimal()) #False:-numbers are there but with space,alphabets,special character
print(g,"=",g.isdecimal()) #False:-the isdecimal treating the point as symbol or special character , that's why even presence of decimal number is false
#isdigit - Returns True if all characters in the string are digits
print("\n")
print(" isdigit ".center(50,"*"))
print(a,"=",a.isdigit()) #False:-there is no number present in string
print(b,"=",b.isdigit()) #False:-there is number within the string but with alphabets
print(c,"=",c.isdigit()) #True:-because of only numbers
print(d,"=",d.isdigit()) #False:-only alphabets are present
print(e,"=",e.isdigit()) #False:-blank space
print(f,"=",f.isdigit()) #False:-numbers are there but with space,alphabets,special character
print(g,"=",g.isdigit()) #False:-the isdigit treating the point as symbol or special character , that's why even presence of decimal number is false

#isnumeric - Returns True if all characters in the string are numeric
print("\n")
print(" isnumeric ".center(50,"*"))
print(a,"=",a.isnumeric()) #False:-there is no number present in string
print(b,"=",b.isnumeric()) #False:-there is number within the string but with alphabets
print(c,"=",c.isnumeric()) #True:-because of only numbers
print(d,"=",d.isnumeric()) #False:-only alphabets are present
print(e,"=",e.isnumeric()) #False:-blank space
print(f,"=",f.isnumeric()) #False:-numbers are there but with space,alphabets,special character
print(g,"=",g.isnumeric()) #False:-isnumeric() doesn't accept decimal points, only numeric characters

#islower - Returns True if all cased characters in the string are lowercase
print("\n")
print(" islower ".center(50,"*"))
print(a,"=",a.islower()) # False: First character is uppercase
print(b,"=",b.islower()) # False: First character is uppercase
print(c,"=",c.islower()) # False: No cased characters (only digits)
print(d,"=",d.islower()) # False: All characters are uppercase
print(e,"=",e.islower()) # False: No cased characters (only spaces)
print(f,"=",f.islower()) # False: First character is uppercase
print(g,"=",g.islower()) # False: No cased characters (only digits and decimal)

#isupper - Returns True if all cased characters in the string are uppercase
print("\n")
print(" isupper ".center(50,"*"))
print(a,"=",a.isupper()) # False: First character is uppercase but others are lowercase
print(b,"=",b.isupper()) # False: Mixed case (first uppercase, rest lowercase)
print(c,"=",c.isupper()) # False: No cased characters (only digits)
print(d,"=",d.isupper()) # True: All alphabetic characters are uppercase
print(e,"=",e.isupper()) # False: No cased characters (only spaces)
print(f,"=",f.isupper()) # False: Mixed case (first uppercase, rest lowercase)
print(g,"=",g.isupper()) # False: No cased characters (only digits and decimal)

#isspace - Returns True if all characters in the string are whitespaces
print("\n")
print(" isspace ".center(50,"*"))
print(a,"=",a.isspace()) # False: Contains non-whitespace characters
print(b,"=",b.isspace()) # False: Contains non-whitespace characters
print(c,"=",c.isspace()) # False: Contains digits (non-whitespace)
print(d,"=",d.isspace()) # False: Contains alphabetic characters
print(e,"=",e.isspace()) # True: Contains only whitespace characters
print(f,"=",f.isspace()) # False: Contains non-whitespace characters
print(g,"=",g.isspace()) # False: Contains digits and decimal point

#istitle - Returns True if the string is titlecased (first character of each word uppercase, rest lowercase)
print("\n")
print(" istitle ".center(50,"*"))
print(a,"=",a.istitle()) # True: Single word with first letter uppercase, rest lowercase
print(b,"=",b.istitle()) # True: Single word with first letter uppercase, rest lowercase+digits
print(c,"=",c.istitle()) # False: No alphabetic characters to be titlecased
print(d,"=",d.istitle()) # False: All letters uppercase (should be only first letter uppercase)
print(e,"=",e.istitle()) # False: No words to be titlecased
print(f,"=",f.istitle()) # True: "Hello" is titlecased, "123@" is not a word so doesn't affect
print(g,"=",g.istitle()) # False: No alphabetic characters to be titlecased

"""
#OUTPUT
******************** isalnum *********************
Hello = True
Hello123 = True
123456 = True
HELLO = True
     = False
Hello 123@ = False
1.234 = False


******************** isalpha *********************
Hello = True
Hello123 = False
123456 = False
HELLO = True
     = False
Hello 123@ = False
1.234 = False


******************* isdecimal ********************
Hello = False
Hello123 = False
123456 = True
HELLO = False
     = False
Hello 123@ = False
1.234 = False


******************** isdigit *********************
Hello = False
Hello123 = False
123456 = True
HELLO = False
     = False
Hello 123@ = False
1.234 = False


******************* isnumeric ********************
Hello = False
Hello123 = False
123456 = True
HELLO = False
     = False
Hello 123@ = False
1.234 = False


******************** islower *********************
Hello = False
Hello123 = False
123456 = False
HELLO = False
     = False
Hello 123@ = False
1.234 = False


******************** isupper *********************
Hello = False
Hello123 = False
123456 = False
HELLO = True
     = False
Hello 123@ = False
1.234 = False


******************** isspace *********************
Hello = False
Hello123 = False
123456 = False
HELLO = False
     = True
Hello 123@ = False
1.234 = False


******************** istitle *********************
Hello = True
Hello123 = True
123456 = False
HELLO = False
     = False
Hello 123@ = True
1.234 = False

"""