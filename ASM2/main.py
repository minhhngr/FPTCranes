from services.enrollment_manage import EnrollmentManager
from services.course_manage import CourseManager
from services.student_manage import StudentManager
from common.config import ProjectPath
from models.student import Student
from models.person import Person


MENUS = (
    "Exit",
    "Load all data",
    "Show all students",
    "Add new student",
    "Remove student",
    "Update student info",
    "Find student by name",
    "Show top N GPA students",
    "Statistics by major",
    "Show students grouped by year",
    "Enroll student to course",
    "Undo last enrollment",
    "Show student courses",
    "Save all data to CSV",
)

menu_selector = dict(enumerate(MENUS))


def show_menu():
    print("========= STUDENT MANAGEMENT =========")
    for k, v in menu_selector.items():
        print(f"{k}. {v}")


student_manage = StudentManager()
course_manage = CourseManager()
enrollment_manage = EnrollmentManager()

if __name__ == "__main__":
    while True:
        choice = input("Input your choice: ")
        if choice == "0":
            break
        elif choice == "1":
            student_manage.load()
            course_manage.load()
            enrollment_manage.load()
        elif choice == "2":
            student_manage.show()
        elif choice == "3":
            pass
        elif choice == "4":
            student_manage.remove(input("Student ID: "))
        elif choice == "5":
            pass
        elif choice == "6":
            pass
        elif choice == "7":
            for s in student_manage.top_n():
                print(s.to_row())
        else:
            print("Invalid your input, please input again")
