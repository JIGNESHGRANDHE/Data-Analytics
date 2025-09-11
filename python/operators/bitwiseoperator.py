# to find the binary of an any number function bin() is used.
binary= int(input("enter a number="))
print("Binary form of entered number is",bin(binary))


l=int(input("\nenter a number="))
b=int(input("enter a number="))
print("binary form of",(l),"is" ,bin(l))
print("binary form of",(b),"is",bin(b))
# AND operator
print("\nAND(&) operator =",l & b)
print(bin(l & b))

# OR operator
print("\nOR(|) operator=",l | b)
print(bin(l | b))

# XOR operator
print("\n XOR(^) operator",l ^b)
print(bin(l ^b))

# Left shift (multiplies by 2^b)
print("\nLeft shift =", l << b)
print("Binary:", bin(l << b))

# Right shift (divides by 2^b)
print("\nRight shift =", l >> b)
print("Binary:", bin(l >> b))


"""
#OUTPUT
enter a number=7
Binary form of entered number is 0b111

enter a number=12
enter a number=3
binary form of 12 is 0b1100
binary form of 3 is 0b11

AND(&) operator = 0
0b0

OR(|) operator= 15
0b1111

 XOR(^) operator 15
0b1111

Left shift = 64
Binary: 0b1000000

Right shift = 0
Binary: 0b0
"""