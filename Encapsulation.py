#encapsulation is about protecting data and only revealing the necessary information

"""to create a private atttribute in the class we use the double underscore """
class student:
    def __init__(self,name,age):

        self.name = name
        self.__age = None
        self.set_age(age)
        
        
    def get_age(self):
      return self.__age


    def set_age(self,age):
        if isinstance(age,int) and 0 <= age <= 120:
           self.__age = age
        else:
           raise ValueError("Age cannnot be negative, it must be between 1 and 120")    
    def get_details(self):
        aged = self.get_age()
        return f"Name : {self.name} and age: {aged} "
    
student1 = student("John",20)
student2 = student('Mary',40)

print(student1.get_details())
print(student2.get_details())

class student_mark:
   def __init__(self,mark):
    self.__mark = mark
    self.set_mark(mark)
    
   def get_mark(self):
       return self.__mark
    
   def set_mark(self,mark):
      if isinstance(mark,int) and (0 <= mark <= 100):
         self.__mark = mark
      else:
         raise ValueError ("Marks must be between 0 and 100")
        
   def student_score(self):
       return(f"The score of the student is : {self.__mark}")
   
score1  = student_mark(90)
print(score1.student_score())




class account:
   def __init__(self,balance):
      self.__balance = None
      self.set_balance(balance)

   def get_balance(self):
      return self.__balance
   
   def set_balance(self,balance):
      if balance <= 100:
         print(f"Low amount {balance} sh to set in the account")
      else:
         self.__balance = balance
   
   def display_balance(self):
      account_balance = self.get_balance()
      print(f'ACCOUNT BALANCE : {account_balance}')
      


acc1 = account(160)
acc2 = account(900)
acc1.display_balance()
acc2.display_balance()

      




      

   