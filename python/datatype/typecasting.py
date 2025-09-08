#Explicit Type conversion

"""int to float conversion"""
a=int(input("enter number="))
print(a)
print(type(a))
a=float(a)
print(a)
print(type(a))
#OUTPUT
"""
enter number=15
15
<class 'int'>
15.0
<class 'float'>
"""

"""float to int conversion"""
a=float(input("enter number="))
print(a)
print(type(a))
a=int(a)
print(a)
print(type(a))
#OUTPUT
"""
enter number=15.4
15.4
<class 'float'>
15
<class 'int'>
"""


"""int to str conversion"""
a=int(input("enter number="))
print(a)
print(type(a))
a=str(a)
print(a)
print(type(a))
#output

"""enter number=14
14
<class 'int'>
14
<class 'str'>"""


"""Implicit conversion"""
c=20
print(c)
print(type(c))
n=5.6
print(n)
print(type(n))
w=c+n
print(w)
print(type(w))

#OUTPUT
"""
20
<class 'int'>
5.6
<class 'float'>
25.6
<class 'float'>
"""