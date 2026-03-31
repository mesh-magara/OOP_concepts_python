class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        return ("HELLO "+ self.name)
    
    def age_checker(self):
        if self.age <= 10:
            print("You are a child")
        elif self.age >= 11 and self.age <= 17:
            print("You are  a minor by the law")
        else:
            print("You are an adult")
        
    def wecloming(self):
        message = self.greet()

        print (message + "! Welcomme to our website and feek free to enjoy")

per1 = Person("meshack",19)
print(per1.greet())
per1.age_checker()
per1.wecloming()

class car:
    def __init__(self, name,brand):
        self.name = name
        self.brand = brand

    def output(self):
        outputed = {}
        
        outputed.update({"Name" : self.name})
        outputed.update({"Brand" : self.brand})
        
        return outputed
    
    def printed(self):
        message = self.output()
        print(f"The car is of {message}")
    

car1 = car("Corolla","TOYOTA")
print(car1.output())
car1.printed()