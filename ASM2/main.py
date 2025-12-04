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

if __name__ == "__main__":
    student_manage.load()
    print(student_manage.count)
    student_manage.save(str(ProjectPath.DATA_PATH / "data.csv"))
    # print(student_manage.min_gpa)
    print(student_manage.search_by_name("Hoàng Văn Lâm"))

    # print(ProjectPath.DATA_PATH)
    # # show_menu()
    # per = Student()
    # per.name = "Lại Gia Lâm"
    # per.dob = "1994-05-06"
    # per.email = "lamgia@example.com"
    # per.sid = "#01"
    # per.major = "Student"
    # per.gpa = 5
    # per.year = 1994
    # print(repr(per))
    # print(per.to_row())
    # from collections import namedtuple
    # s = namedtuple("Student", ["id", "name", "dob", "email", "major", "year", "gpa"])
    # show_menu()
