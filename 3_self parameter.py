#Understanding self parameter

class Employee:

    def empDetails(self):
        self.name = 'Arun'
        print('Name =',self.name)
        age = 26
#self is not used so age is not associated with any object and can be used only inside this function
        print('Age =',age)

    def printEmployeeDetails(self):
        print('Printing in another method.')
        print('name :',self.name)
        print('Age :',age)  #throws errpr as age is unavailable for this function

e1 = Employee() #creating object to the class
e1.empDetails()
Employee.empDetails(e1) #self is used in the place of e1

e1.printEmployeeDetails()
