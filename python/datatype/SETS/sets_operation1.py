a = {"India", "China", "Nepal", "Bhutan", "Sri Lanka"}
print(a)
"""
#OUTPUT:-
{'India', 'Nepal', 'Bhutan', 'China', 'Sri Lanka'}
"""

# adding an element to the set
a.add("USA")
print(a)
"""
#OUTPUT:-
{'China', 'Nepal', 'India', 'Bhutan', 'Sri Lanka', 'USA'}
"""

# remove (if it exists, else throws an error)
a.remove("USA")
print(a)
"""
#OUTPUT:-
{'China', 'Nepal', 'India', 'Bhutan', 'Sri Lanka'}
"""

# discard (does NOT throw error if not present)
a.discard("Nepal")
print(a)
"""
#OUTPUT:-
{'China', 'India', 'Bhutan', 'Sri Lanka'}
"""

# Copying the set
b = a.copy()
print(b)
"""
#OUTPUT:-
{'India', 'China', 'Sri Lanka', 'Bhutan'}
"""
