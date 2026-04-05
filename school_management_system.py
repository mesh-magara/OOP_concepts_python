name = "s13-0444-43"
names = "s13-0444-43"
print(name.upper())
print(name.upper())
if names == name:
    print("The names are the same")
else:
    print("the names are not the same")

students = {
     "S13-04408-24": {
        "name" : 'Meshack Magara',
        "age" : 20,
        "course" : "Computer Science"
    },
    "S13-09093-24":{
        "name": "John kamau",
        "age" : 19,
        "course": "information technology"
    }
}

def add_Student(reg_no,name,age,course):

    #check if the regno already exists in the records
    new_reg_no  = reg_no.upper()

    values = {"name" : name, "age" : age, "course" : course}
    
    if new_reg_no in students:
        print(f"The student {new_reg_no} already exists in the school")
    else:
        students[reg_no] = values
        print("Succesfully added the student")
    

add_Student("S13-04408-24","Meshack Magara",20,"Information")
for reg_no in students:
    print(reg_no)

def search_student(reg_no):
    new_reg_no = reg_no.upper()

    if new_reg_no in students:
        print(f"{students[new_reg_no]}")
    else:
        print("No such student exists in the school")

regi_no = input("Enter the reg-no : ")
search_student(regi_no)