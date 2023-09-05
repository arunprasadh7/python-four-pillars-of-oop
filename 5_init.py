# __init__() method

class Employee:

    def __init__(self,name):
        self.name = name

    #def employeeDetails(self):
        #self.name = 'Arun'

    def displayEmployeeDetails(self):
        print(self.name)

'''
if we call this method before accesing empdetails it throws error as self.name 
is not declared before displayEmployeeDetails and inorder to prevent it they 
are declared under the init method as it initializes at the beginning
'''

#creating instances/objects
e1 = Employee('Arun')
e2 = Employee('Prasadh')
e1.displayEmployeeDetails()
e2.displayEmployeeDetails()