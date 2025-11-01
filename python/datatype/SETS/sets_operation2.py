
a = {"India", "China", "Nepal", "Bhutan", "Sri Lanka"}
b = {"USA", "Canada", "Brazil"}
c = {"Bhutan", "Sri Lanka"}

# isdisjoint()
# Checks if two sets have no elements in common.
print("# isdisjoint()")
print("a.isdisjoint(b):", a.isdisjoint(b))  # True (no common elements)
print("a.isdisjoint(c):", a.isdisjoint(c))  # False (Bhutan & Sri Lanka are common)
print("-" * 50)

#=issubset()
# Checks if all elements of one set exist in another.
print("# issubset()")
print("a.issubset(b):", a.issubset(b))  # False (a not subset of b)
print("c.issubset(a):", c.issubset(a))  # True  (all elements of c exist in a)
print("-" * 50)

#issuperset()
# Checks if a set contains all elements of another set.
print("# issuperset()")
print("a.issuperset(c):", a.issuperset(c))  # True → a contains all of c
print("c.issuperset(a):", c.issuperset(a))  # False → c doesn’t contain all of a
print("-" * 50)

#update()
# Adds all elements from another set into the current set.
print("# update()")
a.update(b)  # Adds all elements of b into a
print("After a.update(b):", a)

a.update(c)  # Adds elements of c into a (already present)
print("After a.update(c):", a)
print("-" * 50)

# clear()
# Removes all elements from the set.
print("# clear()")
print("Return value of a.clear():", a.clear())  # Returns None
print("After clear, a =", a)  # Empty set
print("-" * 50)
