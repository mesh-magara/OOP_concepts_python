class calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def modify(self):
        self.a *= 100
        self.b *= 5

        return self.a , self.b

    def add(self):
        return (self.a + self.b)
    
    def multiply(self):
        return (self.a * self.b)
    
    def divide(self):
        return (self.a / self.b)
    
    def subtract(self):
        return (self.a - self.b)
    
    def display_result(self):
        print(f"Addition : {self.add()}")
        print(f"Subtraction : {self.subtract()}")
        print(f"Multiplication : {self.multiply()}")
        print(f"Division : {self.divide()}")

x  = int(input("Enter the first number : "))
y = int(input("Enter the second number : "))

calc = calculator(x,y)
print(calc.modify())
calc.display_result()

class person:
    def __init__(self, name ,age):
        self.name = name
        self.age = age

    def __str__(self):
        return  f"My name is {self.name} and i am {self.age} years old"

p1 = person(name = "kaligraph" ,age = 40)
print(p1)

"""classes  can have mulitiple methods that each work together """
class playlist:
    def __init__(self,name):
        self.name = name
        self.songs = ["POP","kill","MOCKING BIRD"]

    def add_song(self, song):
        self.songs.append(song)
        print(f"Added song '{song}' to {self.name} playlist")
    
    def remove_song(self,song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Removed '{song}' from {self.name} playlist")
        else:
            print(f"{song} not in the playlist")
    
    def show_songs(self):
        for song in self.songs:
            print(f"- {song} ")

myplaylist = playlist("Favourites")
myplaylist.add_song("Going bad")
myplaylist.add_song("Never say never")
myplaylist.add_song("Chrismass tress")
myplaylist.remove_song("Chrismass tress")
myplaylist.show_songs()


class account:
    def __init__(self,balance):
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print(f"DEPOSIT : {amount} BALANCE : {self.balance}")
    
    def withdraw(self,amount):
        if amount >= self.balance:
            print(f"Cannot withdraw {amount} Insufficient funds in the account")
        else:
            self.balance -= amount
            print(f"WITHDRAW : {amount} BALANCE : {self.balance}")

    def show_balance(self):
        print(f"ACCOUNT BALANCE : {self.balance}")

myaccount = account(1000)
myaccount.deposit(100)
myaccount.deposit(300)
myaccount.deposit(1300)
myaccount.deposit(4000)
myaccount.withdraw(200)
myaccount.withdraw(3000)
myaccount.withdraw(5000)

myaccount.show_balance()