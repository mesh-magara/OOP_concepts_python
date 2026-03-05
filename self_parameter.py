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