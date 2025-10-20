# Dictionary Methods Demonstration
nation = {"name": "India", "capital": "Delhi", "currency": "Rupees"}

# setdefault :- Adds a new key-value pair
nation.setdefault("population", "1.4 Billion")
print("After setdefault:", nation)
"""
OUTPUT: 
After setdefault: {'name': 'India', 'capital': 'Delhi', 'currency': 'Rupees', 'population': '1.4 Billion'}
"""

# update :- Updates the existing dictionary with new key-value pairs
nation.update({"continent": "Asia"})
print("After update:", nation)
"""
OUTPUT:
After update: {'name': 'India', 'capital': 'Delhi', 'currency': 'Rupees', 'population': '1.4 Billion', 'continent': 'Asia'}
"""

# pop :- Removes the specified key and returns its value
removed = nation.pop("continent")
print("Removed item:", removed)
print("After pop:", nation)
"""
OUTPUT:
Removed item: India
After pop: {'capital': 'Delhi', 'currency': 'Rupees', 'population': '1.4 Billion', 'continent': 'Asia'}
"""


# clear :- Removes all items from the dictionary
nation.clear()
print("After clear:", nation)
"""
OUTPUT:
After clear: {}
"""
