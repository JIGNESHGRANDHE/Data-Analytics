a = ("apple", "Cherry", "Banana", "Kiwi", "Strawberry")
print(a)                   #('apple', 'Cherry', 'Banana', 'Kiwi', 'Strawberry')
print(type(a))             #<class 'tuple'>
print(len(a))              # 5

print(a[1:3])              #('Cherry', 'Banana')
print(a[:3])               #('apple', 'Cherry', 'Banana')
print(a[2:])               #('Banana', 'Kiwi', 'Strawberry')
print(a[0::2])             #('apple', 'Banana', 'Strawberry')
print(a[::-1])             #('Strawberry', 'Kiwi', 'Banana', 'Cherry', 'apple')
print(a[2::-1])            #('Banana', 'Cherry', 'apple')
