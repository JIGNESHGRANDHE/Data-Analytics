#Iteration in dictionary
student_1={"name":"Fed", "age":22, "gender":"male", "job":"Engineer"}

#printing all the key names one by one
#Method_1
for q in student_1:
    print(q)

"""
OUTPUT:-
name
age
gender
job
"""

#Method_2
for q1 in student_1.keys():
    print(q1)

"""
OUTPUT:-
name
age
gender
job
"""


#printing all the value name one by one
#Method 1:-
for d in student_1:
    print(student_1[d])

"""
OUTPUT:-
Fed
22
male
Engineer
"""
#Method 2:-using value function
for x in student_1.values():
    print(x)

"""
OUTPUT:-
Fed
22
male
Engineer
"""


#using items function for printing both key and value same time
for k, v in student_1.items():
    print(k,"-",v)

"""
OUTPUT:-
name - Fed
age - 22
gender - male
job - Engineer
"""
