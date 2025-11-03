
a = {"India", "China", "Nepal", "Bhutan", "Sri Lanka"}
b = {"USA", "Canada", "Brazil"}
c = {"Bhutan", "Sri Lanka"}

#  Union
print("# union()")
print("a.union(b):", a.union(b))  # {'Nepal', 'USA', 'Brazil', 'China', 'Bhutan', 'Canada', 'India', 'Sri Lanka'}
print("a.union(c):", a.union(c))  # {'Nepal', 'China', 'Bhutan', 'India', 'Sri Lanka'}
print("*" * 50)

#  Difference
print("# difference()")
print("a.difference(c):", a.difference(c))  # {'Nepal', 'China', 'India'}
print("*" * 50)

#  Difference Update
print("# difference_update()")
a_copy = a.copy()
a_copy.difference_update(c)
print("After difference_update (a - c):", a_copy)  # {'Nepal', 'China', 'India'}
print("*" * 50)

# Reset 'a'
a = {"India", "China", "Nepal", "Bhutan", "Sri Lanka"}

#  Intersection
print("# intersection()")
x = a.intersection(c)
print("a.intersection(c):", x)  # {'Bhutan', 'Sri Lanka'}
print("*" * 50)

#  Intersection Update
print("# intersection_update()")
a_copy = a.copy()
a_copy.intersection_update(c)
print("After intersection_update with c:", a_copy)  # {'Bhutan', 'Sri Lanka'}
print("*" * 50)

# Reset 'a'
a = {"India", "China", "Nepal", "Bhutan", "Sri Lanka"}

#  Symmetric Difference
print("# symmetric_difference()")
y = a.symmetric_difference(c)
print("a:", a)  # {'India', 'China', 'Nepal', 'Bhutan', 'Sri Lanka'}
print("a.symmetric_difference(c):", y)  # {'India', 'China', 'Nepal'}
print("*" * 50)

#  Symmetric Difference Update 
print("# symmetric_difference_update()")
a_copy = a.copy()
a_copy.symmetric_difference_update(c)
print("After symmetric_difference_update:", a_copy)  # {'India', 'China', 'Nepal'}
print("*" * 50)
