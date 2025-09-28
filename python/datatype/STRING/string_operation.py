#endswith():- returns True if the string ends with specified value
a="India "
print(("endswith()").center(20))                #OUTPUT
print(a.endswith("dia"))                        #False
print(a.endswith(" "))                          #True
print(a.endswith("i",0,4))                      #True
print(a.endswith("y",0,4))                     #False
print(a.endswith("a"))                         #False
print(a.endswith("."))                         #False
#startswith():- returns True if the string starts with specified value
print("*"*50)
print(("startswith()").center(20))                  #OUTPUT
print((a.startswith(".")))                          #False
print((a.startswith("i")))                          #False
print((a.startswith("I")))                          #True
print((a.startswith("d",2,5)))                      #True
print(a.startswith("India"))                        #True
#swapcase():- swap cases , lower becomes upper and vice versa
print("*"*50)
print(("swapcase()").center(20))              #OUTPUT
b="Chemistry"                                 #cHEMISTRY
b1="cHEMISTRY"                                #Chemistry
b2="ChEmIsTrY"                                #cHeMiStRy
print(b.swapcase(),"\n",b1.swapcase(),"\n",b2.swapcase())
#strip():- Removes all specified characters from the start and end of the string
print("*"*50)
print(("strip()").center(20))
c="44444   YNew York07   ###"
print(c)
print(c.strip("4, ,#"))
print(c.strip("4,Y,0,7, ,#"))
"""
OUTPUT
44444   YNew York07   ###
YNew York07
New York0
"""
#split():-splits the string at the specified separators and returns a list
print("*"*50)
print(("split()").center(20))
d1="Hi.I am J.I love to play cricket"
d="#YOLO#GOA#Waves#BLUE#sea"
print(d)
print(d.split())
print(d.split("#"))
print(d1.split("."))
#ljust():-return a left justified version of the string
print("*"*50)
print(("ljust()").center(20))
g="Missile man of India"
x="President of India"
print(x.ljust(20),g)
print(x.ljust(20,"*"),g)
"""
#OUTPUT
President of India   Missile man of India
President of India** Missile man of India
"""
#rjust():-return a right justified version of the string
print("*"*50)
print(("rjust()").center(20))
g="Missile man of India"
x="President of India"
print(x.rjust(20),g)
print(x.rjust(20,"*"),g)
"""
#OUTPUT
  President of India Missile man of India
**President of India Missile man of India
"""
#replace():- return a string where a specified value is replaced with a specific value
print("*"*50)
print(("replace()").center(20))
f="Earth is fourth number planet in solar system "
print(f.replace(" ","_"))
print(f.replace("Earth","Mars"))
"""
OUTPUT
Earth_is_fourth_number_planet_in_solar_system
Mars is fourth number planet in solar system
"""
#rindex #rfind  :-Searches the string for a specified value & returns the last position of where is found
print("*"*50)
print(("rindex() and rfind()").center(30))
g="Fruit Orange is from Lemon family"           #OUTPUT
print(g.rindex("o"),g.rindex("O"))              # 24 6
print(g.rfind("o"),g.rfind("O"))                # 24 6
#print(g.index("z"))                            #ERROR
print(g.rfind("z"))                             # -1
print(g.rindex("o",0,20))                       # 18
print(g.rfind("o",0,20))                        # 18
