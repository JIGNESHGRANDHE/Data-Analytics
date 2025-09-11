#logical operators
# OR

"""TRUE if both or one of the operands is true """
"""FAlSE if both operands are false"""
                    #OUTPUT
a= 3<6 or 6>3
print(a)            #True
b= 2==3 or 4!=3
print(b)            #True
c= 1<0 or 4<=2
print(c)            #False


#AND
"""TRUE if both operands are true"""
"""FALSE if one of the operands is false"""
"""FALSE if both operands are false"""
                                #OUTPUT
a= 3<6 and 6>3
print("3<6 and 6>3",a)          #3<6 and 6>3 True
b= 2==3 and 4!=3
print("2==3 and 4!=3",b)        #2==3 and 4!=3 False
c= 1<0 and 4<=2
print("1<0 and 4<=2",c)         #1<0 and 4<=2 False


# NOT
"""TRUE if operand is false"""
"""FALSE if operand is true"""

                #OUTPUT
an= not a
print(an)       #False
bn= not b
print(bn)       #True
cn= not c
print(cn)       #True
