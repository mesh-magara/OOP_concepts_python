class animal:
    def sound(self):
        print("Animal makes sound")
    
class dog(animal):
    def sound(self):
        print("Dogs do bark")

an1 = animal()
an2 = dog()

an1.sound()
an2.sound()

#create a parent class
class person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    
    def get_person_details(self):
        print(f"First-name : {self.fname}\n Last_name : {self.lname}")

x = person("john",'doe')
x.get_person_details()

#create a child class
class student(person):   #the student class inherits from the parent class person
    def __init__(self,fname,lname,age):
        super().__init__(fname,lname)
        self.age = None
        self.set_age(age)
    
    def get_age(self):
        return self.age
    
    def set_age(self,age):
        if age < 0:
            print("Age cannot be negative")
        else:
            self.age = age
        
    def get_student_details(self):
        print(f"Name : {self.fname +" " + self.lname} Age : {self.age}")
    




y = student("mary",'joseph',24)
y.get_student_details()

class account:
    def __init__(self,balance):
        self.__balance = balance
        self.set_balance(balance)
    
    def get_balance(self):
        return self.__balance

    def set_balance(self,balance):
        if balance < 100:
            print(f"you cannot deposit {balance}sh as your initial deposit, 🥲 it must be above 100shs")
            self.__balance = 0
        else:
            self.__balance = balance
    
class transaction(account):
    def __init__(self,balance):
        account.__init__(self,balance)
        self.__balance = balance 
    
    def deposit(self,amount):
        balance = self.get_balance()
        new_balance = balance + amount
        self.set_balance(new_balance)

        print(f"Deposited : {amount}")
        print(f"ACCOUNT BALANCE  : {new_balance}")
    
    def withdraw(self,amount):
        balance = self.get_balance()

        if balance < amount:
            print("Insufficient funds to make such a withdrawal")
        else:
            new_balance = balance - amount
            self.set_balance(new_balance)
            print(f"WITHDREW : {amount}")
            print(f"BANK BALANCE : {new_balance}")
    
    def show_balance(self):
        print(f"THE TOTAL ACCOUNT BALANCE IS : {self.get_balance()}")

acc1 = transaction(150)

dpsit = int(input("How wmuch do you want to deposit ? :: "))
acc1.deposit(dpsit)

wtdrw = int(input("How much do you want to withdraw :: "))
acc1.withdraw(wtdrw)

acc1.show_balance()