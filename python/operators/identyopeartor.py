#Identyty Operators

a=1234
b=1234
w=254

print("\nis Operator")
print("a is b=",a is b)
print("b is a=",b is a)
print("w is b=",w is b)
print("a is w=",a is w)

print("\nis not Operator")
print("a is not b=",a is not b)
print("b is not a=",b is not a)
print("w is not b=",w is not b)
print("w is not b=",w is not b)


"""
#OUTPUT
is Operator
a is b= True
b is a= True
w is b= False
a is w= False

is not Operator
a is not b= False
b is not a= False
w is not b= True
w is not b= True
"""