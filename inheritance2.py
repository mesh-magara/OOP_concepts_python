class user:
    def __init__(self,names,age,id):
        self.name =  names
        self.age = age
        self.__id = None
        self.set_id(id)
    
    def get_id(self):
        return self.__id
    
    def set_id(self,id):
        if isinstance(id,int):
            self.__id = id
        else:
            print("cannot set up a non integer id")
    
    def get_details(self):
        print("-----------***********----------")
        print(f"name : {self.name}")
        print(f"age : {self.age}")
        print(f"ID : {self.get_id()}")

#creating a child classes teacher ,student and worker that both inherits from the user class

class teacher(user):
    def __init__(self,name,age,id,subject,salary):
        super().__init__(name, age, id)
        self.subject = subject
        self.salary = salary
    
    def get_details(self):
        print("-----------***********----------")
        super().get_details()
        print(f"Subject teaching : {self.subject}")
        print(f"Earning : {self.salary} sh")
    
class student(user):
    def __init__(self, name, age, id, course, fees, sport):
        super().__init__(name, age, id)
        self.course = course
        self.fees = fees
        self.sport = sport

    
    def get_details(self):
        print("-----------***********----------")
        super().get_details()
        print(f"Course : {self.course}")
        print(f"Sport : {self.sport}")
        print(f"Fees paid : {self.fees}")


class worker(user):
    def __init__(self, name, age, id ,role,salary):
        super().__init__(name, age, id)
        self.role = role
        self.salary = salary
    
    def get_details(self):
        print("-----------***********----------")
        super().get_details()
        print(f"Role : {self.role}")
        print(f"Salary : {self.salary}")
    
teacher1 = teacher('james',14,3343434,"computer science",90000)
teacher1.get_details()

student1 = student("mart",23,909033,'Information Technology',45000,'Hockey')
student1.get_details()

#Test worker
worker1 = worker("Siminyu",35,2323232,'Store keeper',20000)
worker1.get_details()