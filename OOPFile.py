class Student:
    def __init__(self):
        self.year_defer = ""
        self.module_enrol = ""
        self.student_firstname = ""
        self.student_lastname = ""
        self.student_id = ""
        self.average_grade = ""
        self.course_code = ""
        self.change_module = ""

    def enrol_module(self):
        self.module_enrol = input("Please insert module name to transfer to:")

    def defer_year(self):
        self.year_defer = input("Do you wish to defer the year?:")

    def take_test(self):
        print(self.student_firstname + " " + self.student_lastname + " is taking a test")


def student_data_gather(student):
    student.student_id = input("Please insert your student number:")
    student.student_firstname = input("Please insert first name:")
    student.student_lastname = input("Please insert last name:")
    student.course_code = str(input("Please insert course name:"))
    student.average_grade = input("Please insert " + student.student_firstname + " " + student.student_lastname + "'s average grade")
    student.defer_year()

    if student.year_defer == "Yes":
        print("You are deferring a year")
    else:
        pass
    student.change_module = input("Do you wish to change module?:")

    if student.change_module == "Yes":
        student.enrol_module()
    else:
        pass
    student.take_test()


def student_data_dump(student):
    print("Name : " + student.student_firstname + " " + student.student_lastname)
    print("Student ID : " + student.student_id)
    print("Average Grade : " + student.average_grade)
    print("Module : " + student.course_code)
    print("Wish to defer year? : " + student.year_defer)
    print("New Module enrol : " + student.module_enrol)


William = Student()
Paul = Student()

student_data_gather(William)
student_data_gather(Paul)

print("Student Data:")

student_data_dump(William)
student_data_dump(Paul)
