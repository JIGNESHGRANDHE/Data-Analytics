
# Function 1: Add two numbers
def add(a, b):
    print(a + b)

add(1, 2)  # 3
add(3, 4)  # 7


# Function 2: Calculate the area of a rectangle
def area(length, width):
    print("Area of Rectangle is", length * width)

area(3, 4)
"""
OUTPUT:-
Area of Rectangle is 12
"""

# Function 3: Greet using variable-length arguments
def hello(*names):
    print("Hello, my name is", names[2])

hello("Jack", "Oggy", "Lisa")

"""
OUTPUT:-
Hello, my name is Lisa
"""