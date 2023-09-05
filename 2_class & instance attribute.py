#class & instance attribute

class Employee:
    workingHours = 40   #class attribute

e1 = Employee()
e1.workingHours
#to change class attribute - change it to 50 - call it using class name
Employee.workinghours = 50

e1.name = 'Arun'
e1.name
'Arun'
e2 = Employee()
e2.name = 'Prasadh'
e2.name
'Prasadh'

e1.workingHours = 50 #changes working hours for e1 from 40 to 50


