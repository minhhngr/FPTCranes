from contextlib import suppress

from models.exceptions import CourseNotFoundException, StudentNotFoundException
from services.course_manage import CourseManager
from services.student_manage import StudentManager


def find_student_by_id(sm: StudentManager):
    while True:
        with suppress(Exception):
            sid = input("Input > SID: ")
            return sm.students[sid]

        anws = input(f"Student ID not exist: {sid!r}, please try input again (y/n): ")
        if anws.lower().strip() == "n":
            return


def find_course_by_id(cm: CourseManager):
    while True:
        with suppress(Exception):
            cid = input("Input > CID: ")
            return cm.courses[cid]

        anws = input(f"Course ID not found: {cid!r}, please try input again (y/n): ")
        if anws.lower().strip() == "n":
            return
