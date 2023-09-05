#Multiple inheritance

class OperatingSystem:
    multitasking = True
    name = 'Mac OS'

class Apple:
    website = 'www.apple.com'
    name = 'Apple'

class MacBook(OperatingSystem,Apple):
    def __init__(self):
        if self.multitasking == True:
            print(f'This is a multi-tasking system. Visit {self.website} for more details.')
            print('Name :',self.name)

macbook = MacBook()
