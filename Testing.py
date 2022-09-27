from enum import Enum
import abc
from json import JSONDecodeError

class TaxiColour(Enum):
    RED = 'r'
    GREEN = 'g'

class Taxi(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def say_goodbye():
        pass

    @abc.abstractclassmethod
    def getDistanceToT2():
        pass

class NTTaxi:

    def __init__(self):
        self.initFee = 20.5
        self.t1Fee = 1.5
        self.t2Fee = 1.2
        self.maxT1Fee = 65.5

    def say_goodbye(self, name: str):
        print("Thanks for taking the NT taxi, see you next time", name + "!")

    def getDistanceToT2(self):
        return (self.maxT1Fee - self.initFee) / self.t1Fee * 0.2

class UrbanTaxi:
    def __init__(self):
        self.initFee = 24
        self.t1Fee = 1.7
        self.t2Fee = 1.2
        self.maxT1Fee = 83.5
    
    def say_goodbye(self, name):
        print("Thanks for taking the Urban taxi, see you next time", name + "!")

    def getDistanceToT2(self):
        return (self.maxT1Fee - self.initFee) / self.t1Fee * 0.2

class TaxiFactory:
    def __init__(self) -> None:
        pass

    def create_taxi(self, taxiColour: TaxiColour):
        if taxiColour == TaxiColour.RED.value:
            return UrbanTaxi()
        elif taxiColour == TaxiColour.GREEN.value:
            return NTTaxi()

class FeeCalculator:
    def __init__(self, name = '', taxiType = '', distance = 0):
        self.name = name
        self.taxiType = taxiType
        self.distance = distance

    def getTaxiType(self):
        taxiFactory = TaxiFactory()
        while True:
            self.taxiType = input("Usage: type in prompt [ r / red ] for urban taxi or [ g / green ] for NT taxi\n").lower()
            if self.taxiType == 'r' or self.taxiType == 'red':
                self.taxiType = taxiFactory.create_taxi('r')
                break
            elif self.taxiType == 'g' or self.taxiType == 'green':
                self.taxiType = taxiFactory.create_taxi('g')
                break

    def getDistance(self):
            try:
                self.distance = float(input("Usage: the distance must be a number "))
            except:
                self.getDistance()

    def calFee(self) -> float:
        if self.distance <= 2:
            return self.taxiType.initFee
        elif self.distance - 2 <= self.taxiType.getDistanceToT2():
            return self.taxiType.initFee + int((self.distance - 2)/ 0.2) * self.taxiType.t1Fee
        else:
            return self.taxiType.initFee + int((self.distance - 2) / 0.2) * self.taxiType.t1Fee - int((self.distance - 2 - self.taxiType.getDistanceToT2()) / 0.2) * (self.taxiType.t1Fee - self.taxiType.t2Fee)

def main():
    print("Hello welcome to the HK taxi fee calculator")
    feeCalculator = FeeCalculator()
    feeCalculator.name = input("Hey what is your name? ")
    print("Hi", feeCalculator.name)
    print("Are you taking a RED or GREEN taxi?")
    feeCalculator.getTaxiType()
    print("How long is your taxi trip going to be (in km)?")
    feeCalculator.getDistance()
    print("Your trip is $" + str(feeCalculator.calFee()))
    feeCalculator.taxiType.say_goodbye(feeCalculator.name)

if __name__ == "__main__":
    main()