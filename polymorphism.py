"""CLASS POLYMORPHISM BASICS """
class car:
    def __init__(self,brand,name):
        self.brand = brand
        self.name  = name

    def move(self):
        print("The car is moving through driving")
    
class boat:
    def __init__(self,brand,name):
        self.brand = brand
        self.name = name
    
    def move(self):
        print("The boat is sailing across the sea")
    
class plane:
    def __init__(self,brand,name):
        self.brand = brand
        self.name = name
    
    def move(self):
        print("The plane is flying in the sky")
    
car1 = car("TOYOTA","MAZDA")
boat1 = boat("IBIZA",'TOURING-20')
plane1 = plane("BOEING",'747')

for x in (car1,boat1,plane1):
    x.move()
    print("----------------------------")

"""INHERITANCE IN CLASS POLYMORPHISM """
class vehicle:
    def __init__(self,brand,name):
        self.brand = brand
        self.name = name
    
    def motion(self):
        print(f"The vehicle {self.name} is always moving")
    
class Car(vehicle):
    pass

class Boat(vehicle):
    def motion(self):
        print(f"The boat {self.name} is always sailing across the oceans")
    
class Plane(vehicle):
    def motion(self):
        print(f"The plane {self.name} is flying past the clouds in the sky ")

car2 = Car("Toyota","mustang")
boat2 = Boat("indris","sail560")
plane3 = Plane("Airways","kenya")

for y in (car2,boat2,plane3):
    print(y.brand)
    y.motion()
    print("*********************************************")
