# format():- inserts a value inside {} placeholders in a string
a ="HUMAN"
b="{} shared 90% DNA with monkeys & gorillas."
print(b.format(a))
"""
#OUTPUT
HUMAN shared 90% DNA with monkeys & gorillas.
"""

# capitalize():- makes the first letter uppercase and the rest lowercase
c="Lion iS from cAt family "
print(c.capitalize())
"""
#OUTPUT
Lion is from cat family 
"""

# casefold():- converts the entire string into lowercase
d="First BIG house in Town"
print(d.casefold())
"""
#OUTPUT
first big house in town
"""

# center():- Adds characters on both sides to make text appear in middle
print(a.center(20))

print(a.center(13,"|"))
"""
#OUTPUT
       HUMAN        
||||HUMAN||||

"""
