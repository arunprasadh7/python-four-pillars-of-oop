#Overiding in python

class Employee:
    def setNumberOfWorkingHours(self):
        self.numberOfWorkingHours = 40

    def displayNumberOfWorkingHours(self):
        print(self.numberOfWorkingHours)

class Trainee(Employee):
    def setNumberOfWorkingHours(self):
        self.numberOfWorkingHours = 45 #overides work hours from 40 to 45

    def resetNumberOfWorkingHours(self):
        super().setNumberOfWorkingHours() #reassigns work hrs to parent/base class


e1 = Employee()
e1.setNumberOfWorkingHours()
print('Number of working hours of employee: ',end='')
e1.displayNumberOfWorkingHours()

t1 = Trainee()
t1.setNumberOfWorkingHours()
print('Number of working hours of trainee: ',end='')
t1.displayNumberOfWorkingHours()

t1.resetNumberOfWorkingHours()
print('Reset Number of working hours of trainee: ',end='')
t1.displayNumberOfWorkingHours()