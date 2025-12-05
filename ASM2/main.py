from common.common import find_course_by_id, find_student_by_id
from models.enrollment import Enrollment
from utils.validators import catch_exception
from services.enrollment_manage import EnrollmentManager
from services.course_manage import CourseManager
from services.student_manage import StudentManager
from models.student import Student

MENU = (
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
    "Show average GPA by year",
    "Show student GPA based on enrolled courses",
)

menu_selector = {str(k): v for k, v in enumerate(MENU)}

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
        if menu_selector.get(choice):
            print(f"========= {menu_selector.get(choice)} =========")

        # ---------------------------------------------------------- #
        # ---------------------------------------------------------- #
        # ---------------------------------------------------------- #
        if choice == "0":
            break

        # -----------------------------------------------------------
        # Load all data
        # -----------------------------------------------------------
        elif choice == "1":
            student_manage.load()
            course_manage.load()
            enrollment_manage.load()

        # -----------------------------------------------------------
        # Show all students
        # -----------------------------------------------------------
        elif choice == "2":
            student_manage.show()

        # -----------------------------------------------------------
        # Add new student
        # -----------------------------------------------------------
        elif choice == "3":
            stu = Student()
            add_fields = zip(
                StudentManager.StudentsFields._fields,
                ("SID", "Name", "DOB (YYYY-MM-DD)", "Email", "Major", "Year", "GPA"),
            )
            for k, msg in add_fields:
                catch_exception(lambda: setattr(stu, k, input(f"Input > {msg}: ")))

            student_manage.add(stu)

        # -----------------------------------------------------------
        # Remove student
        # -----------------------------------------------------------
        elif choice == "4":
            student_manage.remove(input("Student ID: "))

        # -----------------------------------------------------------
        # Update student info
        # -----------------------------------------------------------
        elif choice == "5":
            student = find_student_by_id(student_manage)
            if not student:
                continue

            add_fields = zip(
                StudentManager.StudentsFields._fields,
                ("SID", "Name", "DOB (YYYY-MM-DD)", "Email", "Major", "Year", "GPA"),
            )

            for field, msg in list(add_fields)[1:]:
                catch_exception(
                    lambda: setattr(
                        student,
                        field,
                        input(f"Inptut > {msg} [{getattr(student, field)}]: ")
                        or getattr(student, field),
                    )
                )

            student_manage.update(student.sid, student=student)

        # -----------------------------------------------------------
        # Find student by name
        # -----------------------------------------------------------
        elif choice == "6":
            find_name = input("Search student by Name: ")
            students = student_manage.search_by_name(find_name)

            if not students:
                print(f"Not found the student: {find_name!r}")
                continue

            for _s in students:
                print(_s)

        # -----------------------------------------------------------
        # Show top N GPA students
        # -----------------------------------------------------------
        elif choice == "7":

            print("Top 5 student GPA Max: ")
            for s in student_manage.top_n():
                print(s.to_row())

            print()
            print("Top 5 student GPA Min: ")
            for s in student_manage.top_n(reverse=False):
                print(s.to_row())

        # -----------------------------------------------------------
        # Statistics by major
        # -----------------------------------------------------------
        elif choice == "8":
            if not student_manage.count_major:
                print("Statistics by major: 0")
            for _maj, _count in student_manage.count_major.items():
                print(f"{_maj}: {_count} students")

        # -----------------------------------------------------------
        # Show students grouped by year
        # -----------------------------------------------------------
        elif choice == "9":
            for _year, lst in student_manage.by_years.items():
                print(f"\nYear {_year}: ")
                for _s in lst:
                    print(f" . SID, Name > {_s.sid}, {_s.name}")

        # -----------------------------------------------------------
        # Enroll student to course
        # -----------------------------------------------------------
        elif choice == "10":
            sid = find_student_by_id(student_manage)
            if not sid:
                continue

            cid = find_course_by_id(course_manage)
            if not cid:
                continue

            enr = Enrollment()
            enr.student_id = sid
            enr.course_id = cid
            catch_exception(lambda: setattr(enr, "mark", input("Input > mark: ")))
            enrollment_manage.enroll(enr)

        # -----------------------------------------------------------
        # Undo last enrollment
        # -----------------------------------------------------------
        elif choice == "11":
            msg = enrollment_manage.undo()
            if msg:
                print(msg)

        # -----------------------------------------------------------
        # Show student courses
        # -----------------------------------------------------------
        elif choice == "12":
            sid = input("Student ID: ")
            for e in enrollment_manage.get_courses_of_student(sid):
                print(e)

        # -----------------------------------------------------------
        # Save all data to CSV
        # -----------------------------------------------------------
        elif choice == "13":
            student_manage.save()
            course_manage.save()
            enrollment_manage.save()

        # -----------------------------------------------------------
        # Show average GPA by year
        # -----------------------------------------------------------
        elif choice == "14":
            rs = student_manage.avg_gpa_by_year()
            for y, gpa in rs.items():
                print(f"Year: {y}, AVG(GPA): {gpa}")

        # -----------------------------------------------------------
        # Avg (GPA) student from course_id
        # -----------------------------------------------------------
        elif choice == "15":
            sid = input("Student id: ")
            result = enrollment_manage.avg_mark(sid)
            print(f"Avg (GPA): {result}")

        else:
            print("Invalid your input, please input again")
