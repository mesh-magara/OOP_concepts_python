"""To create a class you use the keyword class"""
class student:
    name = "meshack magara"

#to create an object from the same class
s1 = student()
print(s1.name)

# You can also delete an object using the key word del
s2 = student()
del s2

# print(s2.name) ""prints not defined because the class is already deleted"""

"""One can also have many objects of the same class """
s3 = student()
s4 = student()
p5 = student()
print(s3.name)
print(s4.name)
print(p5.name)

"you can also create a class but not wish to define the contents of the class"
class reptiles:
    pass

an1 = reptiles()
print(an1.name)
