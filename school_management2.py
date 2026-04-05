"""  CREATING A SIMPLE STUDENT MANAGEMENT SYSTEM  """
students = {}

print(students)
#function that adds student records into the records

def add_Student(reg_no,name,age,course):

    #check if the regno already exists in the records
    new_reg_no  = reg_no.upper()

    values = {"name" : name, "age" : age, "course" : course}

    if new_reg_no in students:
        print(f"The student {new_reg_no} already exists in the student records")
    else:
        students[new_reg_no] = values
        print("Student alreay added successfully")

#function that views the student records
def view_records():
    print(students)

# A function that searches for the student details
def search_student(reg_no):
    new_reg_no = reg_no.upper()

    if new_reg_no in students:
        print(students[new_reg_no])
    else:
        print("No such student exists in the school")

def update_student(reg_no):
            new_reg_no = reg_no.upper()
            if new_reg_no in students:
                print("What do you want to update?")
                print("1. Name")
                print("2. Age")
                print("3. Course")
                print("4.Registration Number")

                update_choice = int(input("Enter your choice (1-3): "))
                if update_choice == 1:
                    new_name = input("Enter new name: ")
                    students[new_reg_no]["name"] = new_name
                    print("Name updated successfully.")
                elif update_choice == 2:
                    new_age = int(input("Enter new age: "))
                    students[new_reg_no]["age"] = new_age
                    print("Age updated successfully.")
                elif update_choice == 3:
                    new_course = input("Enter new course: ")
                    students[new_reg_no]["course"] = new_course
                    print("Course updated successfully.")
                
                elif choice == 4:
                    new_regno = input("Enter the new Registration number : ")
                    new_reg_no = new_regno
                else:
                    print("Invalid choice.")
            else:
                print("The student does not exist in the school.")

def delete_student(reg_no):
     
    new_reg_no = reg_no.upper()
    if new_reg_no  in students:
        del students[new_reg_no]
        print(f"student {new_reg_no} deleted succesfully")
    
    else:
        print("The student does not exist in the school")
    

    
    

for i in range(10):
    print("*********SERVICES*********")
    print("""
      1. Add students
      2. Viewing students
      3. Searching students
      4. Updating students
      5. Deleting students
      6. Exit the program
""")

    choice  = int(input("Enter the number of the service you wish to perfom : "))
    if choice == 1 :
        name  = input("Enter name : ")
        reg_no = input("Enter reg_no : ")
        age = int(input("Enter the age : "))
        course = input("Enter your course : ")

        add_Student(reg_no,name,age,course)
    
    if choice == 2:
        view_records()

    if choice == 3:
        regi_no = input("Enter the reg no (***-*****-24) : ")
        search_student(regi_no)
    
    if choice  == 4:
        regi_no = input("Enter the reg no (***-*****-24) you wish to update : ")
        update_student(regi_no)

    if choice == 5:
        regi_no = input("Enter the reg no (***-*****-24) you wish to delete : ")
        delete_student(regi_no)


    if choice  == 6:
        break




