"""cconstructors in python is using the method __init__ to initialize the objects"""
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    

     #creating objects directly and then initializing them 
    
student1 = Student("james",30)
student2 = Student("Jacob",21)

print(student1.name, student1.age)
print(student2.name, student2.age)

"""you can also have some default parameters """

class animal:
    def __init__(self, name = "unknown",age = 0):
        self.name = name
        self.age = age

cat = animal()
dog = animal("Dog")
cow = animal("cow",6)

print(cat.name, cat.age)
print(cow.name,cow.age)
print(dog.name,dog.age)