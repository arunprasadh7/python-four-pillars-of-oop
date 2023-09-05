"""
Access specifiers - Public Protected and private
Public -  memberName
Protected - _memberName
Private - __memberName
name mangling on private members - __variableName => _ClassName__variableName
"""

class Car:
    numberOfWheels = 4
    _color = 'Black'
    __yearOfManufacture = 2023 # _Car__yearOfManufacture

class Bmw(Car):
    def __init__(self):
        print('Protected color attribute: ',self._color)

car = Car()
print('Public attribute noOfWheels : ',Car.numberOfWheels)

bmw = Bmw()
print('Private attribute yearOfManufacture : ',car._Car__yearOfManufacture)

