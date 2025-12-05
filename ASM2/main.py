from contextlib import suppress
from utils.validators import catch_exception
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

menu_selector = {str(k): v for k, v in enumerate(MENUS)}

student_manage = StudentManager()
course_manage = CourseManager()
enrollment_manage = EnrollmentManager()


if __name__ == "__main__":
    while True:
        print()
        print("========= STUDENT MANAGEMENT =========")
        for k, v in menu_selector.items():
            print(f"{k}. {v}")

        choice = input("Input your choice: ")
        print(f"========= {menu_selector[choice]} =========")
        if choice == "0":
            break
        elif choice == "1":
            student_manage.load()
            course_manage.load()
            enrollment_manage.load()
        elif choice == "2":
            student_manage.show()
        elif choice == "3":
            stu = Student()
            add_fields = zip(
                StudentManager.StudentsFields._fields,
                ("SID", "Name", "DOB (YYYY-MM-DD)", "Email", "Major", "Year", "GPA"),
            )
            for k, msg in add_fields:
                catch_exception(lambda: setattr(stu, k, input(f"Input > {msg}: ")))

            student_manage.add(stu)
        elif choice == "4":
            student_manage.remove(input("Student ID: "))
        elif choice == "5":
            sid = input("Input > SID: ")

            add_fields = zip(
                StudentManager.StudentsFields._fields,
                ("SID", "Name", "DOB (YYYY-MM-DD)", "Email", "Major", "Year", "GPA"),
            )

            st = student_manage.students.get(sid)
            if not st:
                print(f"Not found {sid}")
                break

            for k, msg in list(add_fields)[1:]:
                catch_exception(
                    lambda: setattr(
                        st,
                        k,
                        input(f"Input > {msg} [{getattr(st, k)}]: ") or getattr(st, k),
                    )
                )

            student_manage.update(sid, st)
        elif choice == "6":
            pass
        elif choice == "7":
            for s in student_manage.top_n():
                print(s.to_row())
        elif choice == "8":
            pass
        elif choice == "9":
            pass
        elif choice == "10":
            pass
        elif choice == "11":
            pass
        elif choice == "12":
            pass
        elif choice == "13":
            student_manage.save()
            course_manage.save()
            enrollment_manage.save()
        else:
            print("Invalid your input, please input again")
