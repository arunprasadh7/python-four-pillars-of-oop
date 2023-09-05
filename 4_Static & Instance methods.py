#Stactic and Instance methods
class Employee:

    def employeeDetails(self):
        self.name = 'Arun'

    @staticmethod
    def welcomeMessage():# throws error if self is not used, which can be avoided by using static method
        print('Welcome to our org!!!')

e1 = Employee()
e1.employeeDetails()
print(e1.name)
e1.welcomeMessage()