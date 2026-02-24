#Date:23/02/2026

students=[]

def register_student():
    student_id=input("enter student ID")
    name=input("enter Name:")
    course=input("enter Course:")
    phone=input("enter phone number:")

    student = {
        "id": student_id,
        "name": name,
        "course": course,
        "phone": phone,
        "grade": None
    }
    
    students.append(student)
    print("student registered successfully")

def display_students():
    if not students:
        print("no students registered")
    else:
        for student in students:
            print(student)

def assign_course_and_grade():
    student_id=input("enter student ID to update: ")

    for student in students:
        if student["id"]==student_id:
            new_course=input("enter new course:")
            grade=input("enter grade:")
            student["course"]=new_course
            student["grade"]=grade
            print("updated successfully")
            return
    
    print("student not found")

def main():
    while True:
        print("===School Management System===")
        print("1. register new student")
        print("2. display registered student")
        print("3. assign new course and grade")
        print("4. exit")

        choice=input("choose option:")

        if choice=="1":
            register_student()
        elif choice=="2":
            display_students()
        elif choice=="3":
            assign_course_and_grade()
        elif choice=="4":
            print("exiting system...")
            break
        else:
            print("invalid option. Try again")

if __name__=="__main__":
    main()
