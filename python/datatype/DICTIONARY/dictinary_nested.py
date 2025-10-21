Employees={1:{'name':'Jack','age':25,'emp_id':111,'Gender':'Male'},
           2:{'name':'Julia','age':29,'emp_id':112,'Gender':'Male'},
           3:{'name':'Olly','age':35,'emp_id':113,'Gender':'Female'}}

print(Employees) #{1: {'name': 'Jack', 'age': 25, 'emp_id': 111, 'Gender': 'Male'}, 2: {'name': 'Julia', 'age': 29, 'emp_id': 112, 'Gender': 'Male'}, 3: {'name': 'Olly', 'age': 35, 'emp_id': 113, 'Gender': 'Female'}}

print(Employees[1]) #{'name': 'Jack', 'age': 25, 'emp_id': 111, 'Gender': 'Male'}

print(Employees[2]) #{'name': 'Julia', 'age': 29, 'emp_id': 112, 'Gender': 'Male'}

print(Employees[3]) #{'name': 'Olly', 'age': 35, 'emp_id': 113, 'Gender': 'Female'}

print(Employees[3]['name'],'(',Employees[3]['Gender'],')')  #Olly ( Female )
