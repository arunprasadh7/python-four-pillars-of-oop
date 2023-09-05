#Multi-level inheritance in python

class MusicalInstruments:
    numberOfMajorKeys = 12

class StringInstruments(MusicalInstruments):
    typeOfWood = 'Tone Wood'

class Guitar(StringInstruments):
    def __init__(self):
        self.numberOfStrings = 6
        print(f'This guitar consists of {self.numberOfStrings} strings. '
              f'It is made of {self.typeOfWood} and it can play {self.numberOfMajorKeys} keys.')

guitar = Guitar()