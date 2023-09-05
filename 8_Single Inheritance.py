#Third pillar of oop - inheritance
#Single inheritance

class Apple:    #parent class
    manufacturer = 'Apple Inc'
    website = 'www.apple.com/contact'

    def contactDetails(self):
        print('To contact us, please log on to',self.website)

class Macbook(Apple):   #child class
    def __init__(self):
        self.yearOfManufacture = 2023

    def manufactureDetails(self):
        print(f'This MacBook was manufactured in the year {self.yearOfManufacture} by {self.manufacturer}.')

macBook = Macbook()
macBook.manufactureDetails()
macBook.contactDetails()
