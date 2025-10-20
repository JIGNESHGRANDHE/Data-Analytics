nation={"name":"India","capital":"Delhi","currency":"Rupees"}

# .get :- getting all the values by putting their respective key
print(nation.get("name"))
print(nation.get("capital"))
print(nation.get("currency"))
"""
#OUTPUT:-
India
Delhi
Rupees
"""

#items :- printing all the pair of key & value in dictionary as tuple
print(nation.items())
"""
#OUTPUT:-
dict_items([('name', 'India'), ('capital', 'Delhi'), ('currency', 'Rupees')])
"""

#keys :- printing all the keys in dictionary
print(nation.keys())
"""
#OUTPUT:-
dict_keys(['name', 'capital', 'currency'])
"""

#values :- printing all the values in dictionary
print(nation.values())
"""
#OUTPUT:-
dict_values(['India', 'Delhi', 'Rupees'])
"""

#copy :- creates a duplicate of the existing dictionary.
c={}
print(c)
c=nation.copy()
print(c)
"""
#OUTPUT:-
{}
{'name': 'India', 'capital': 'Delhi', 'currency': 'Rupees'}
"""
