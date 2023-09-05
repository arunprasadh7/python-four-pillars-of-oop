#check if employee has achived his weekly target or not

class Employee:

    name = 'Arun'
    designation = 'Developer'
    weeklyWorkHours = 50

    def target(self):
        if self.weeklyWorkHours >= 50:
            print('Weekly target achieved!')
        else:
            print('Weekly target not achieved.')
