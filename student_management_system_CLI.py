import json

def add_student(): 
    global students
    
    if not students:
        student_id = 1
    else:
        student_id = max(s['student_id'] for s in students) + 1    
    
    while True:
        print(f"Student ID: {student_id}")
        
        try:
            #student name validation
            student_name = input("Student Name: ").strip()
            if not student_name:
                print("Name cannot be left empty")
                continue
                
            if student_name.isdigit():
                print("Please enter correct input") 
                continue
                
            #student age validation    
            student_age = int(input("Student Age: "))
            if student_age <=0 or student_age >=85:
                print("Please enter age between (1 and 84)")
                continue
                
            #student course validation
            student_course = input("Student Course: ").strip()
            if not student_course:
                print("Student course cannot be left empty")
                continue
                
            #student score validation
            student_score = int(input("Student Score: "))
            if not student_score:
                print("Score cannot be left empty")
                continue
                
            #student details(dic)
            student_details = {
                'student_id': student_id,
                'student_name': student_name,
                'student_age': student_age,
                'student_course': student_course,
                'student_score': student_score
            }
            
            students.append(student_details)
            #print(f"Successfully added:\n Student ID: {student_id}\n Student Name: {student_name}")
            
            return student_details
            
        except(ValueError):
            print("Please enter correct input")    
                    
    
def view_student():
    if students:
        for student in students:
            print(student)
    else:
        print("No student in the list")
    


def delete_student():
    if not students:
        print("No student in the list")
    else:
        for student in students:
            print(student)
        
        while True:
            try:
                id_to_delete = int(input("Student you wish to delete (enter student ID): "))
                
                for student in students:
                    if student['student_id'] == id_to_delete:
                        student_name = student['student_name']
                        students.remove(student)
                        print(f"ID: {id_to_delete}, Student name: {student_name} deleted successfully")
                break
            
            except ValueError:
                print("Please enter numeric ID")
    
    
    
def save_student():
    with open('students_data.json', 'w') as f:
        json.dump(students, f)
    print("Student data saved successfully")
    
    
def load_students():
    global students
    try:
        with open('students_data.json', 'r') as f:
            students = json.load(f)
    except(FileNotFoundError):
        students = []
    

students = []
def main():
    while True:       
        print("1. Add new student")
        print("2. View Students")
        print("3. Delete a student")
        print("4. Exit")
        action = input("Select the action(1,2,3,4): ")
                              
        if action == '1':
            add_student()
                    
        elif action == '2':
            view_student()
                    
        elif action == '3':
            delete_student()
                    
        elif action == '4':
            save_student()
            print("Exiting ...")
            exit()
            

load_students()           
main()
    
        







