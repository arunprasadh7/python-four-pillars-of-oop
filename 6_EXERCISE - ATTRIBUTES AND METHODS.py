#EXERCISE - ATTRIBUTES AND METHODS
'''Write an object oriented program to create a precious stone.
Not more than 5 precious stones can be held in possession at a
given point of time. If there are more than 5 precious stones,
delete the first stone and store the new one.'''

class PreciousStone:
    count = 0
    stoneList = []
    def __init__(self):
        name = input('Enter gem name: ')
        self.stoneList.append(name)
        self.count += 1

    def stoneCount(self):
        a = 0
        if len(self.stoneList) < 5:
            for gem in self.stoneList:
                a = 1
        #print(gem)

        elif len(self.stoneList) > 5:
            c = self.stoneList.pop(0)
            c = self.stoneList
            for i in c:
                print(i)


s1 = PreciousStone()
s1.stoneCount()
s2 = PreciousStone()
s2.stoneCount()
s3 = PreciousStone()
s3.stoneCount()
s4 = PreciousStone()
s4.stoneCount()
s5 = PreciousStone()a
s5.stoneCount()
s6 = PreciousStone()
s6.stoneCount()



