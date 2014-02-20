import random
import itertools
from random import choice
from math import sqrt

class country():
    def __iter__(self):
        for item in self.__cities:
            yield item
    
    def __init__(self,aantal, hoogte, breedte):
        self.__cities = []
        
        count = 0
        while count < aantal:
            self.addCity(hoogte, breedte)
            count += 1
    
    def addCity(self, hoogte, breedte):
        self.__cities.append(city(hoogte, breedte))
        
    def printCities(self):
        for c in self.__cities:
            print(c)
    
    def drawCities(self,canvas):
        for c in self.__cities:
            c.draw(canvas)
    
    def getCities(self):
        pass
        
    def createRoute(self):
        pass
    
    def getDistanceBetweenTwoCities(self, citya,cityb):
        return sqrt((cityb.getXLoc()-citya.getXLoc())**2+(cityb.getYLoc()-citya.getYLoc())**2)
        
    def GetClosestCity(self, FromCity):
        closestCity = 0
        distance = 0
        for c in self.__cities:
            if c == FromCity:
                pass
            else:
                if distance == 0 or self.getDistanceBetweenTwoCities(FromCity,c) < distance:
                    distance = self.getDistanceBetweenTwoCities(FromCity,c)
                    closestCity = c
        return closestCity
        
    def getRandomCity(self):
        return choice(self.__cities)
                
    
    def printAllPermutations(self):
        randomCity = self.getRandomCity()
        rlist = []
        for e in itertools.permutations(self):
            if e[0] == randomCity:
                rlist.append(e)
        for i in rlist:
            print(i)
        


        
class city():
    def __init__(self, hoogte, breedte):
        self.__xloc = random.randint(0, hoogte)
        self.__yloc = random.randint(0, breedte)
        
    def __str__(self):
        return '(city @ %s:%s)' % (self.__xloc, self.__yloc)
    
    def __repr__(self):
        return '(city @ %s:%s)' % (self.__xloc, self.__yloc)
        
    def draw(self, canvas):
        canvas.create_oval(self.__xloc,self.__yloc,self.__xloc,self.__yloc)
        
    def getXLoc(self):
        return self.__xloc
    
    def getYLoc(self):
        return self.__yloc
        
class route():
    def __init__(self):
        pass
        
    