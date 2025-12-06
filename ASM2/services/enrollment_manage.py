from collections import Counter, deque, namedtuple

from models.enrollment import Enrollment
from models.exceptions import EnrollmentNotFoundException
from common.config import ProjectPath
from utils import file_handler


class EnrollmentManager:
    _ENROLL_PATH = ProjectPath.DATA_PATH / "enrollments.csv"
    EnrollFields = namedtuple("EnrollFields", ("student_id", "course_id", "mark"))

    def __init__(self):
        self.enrollments = {}
        self.history = deque()
        self.count_course = Counter()

    def show(self):
        if not self.enrollments:
            print("Enrollment is empty")

        for enrollment in self.enrollments.values():
            print(repr(enrollment))

    def enroll(self, enroll: Enrollment, save_history=True):
        self.enrollments.setdefault(enroll.student_id, []).append(enroll)
        self.count_course[enroll.course_id] += 1

        if save_history:
            self.history.append(("add", enroll.student_id, enroll.course_id))

    def undo(self):
        if not self.history:
            return "Nothing to undo"

        op, sid, cid = self.history.pop()
        if op == "add":
            lst = self.enrollments.get(sid, [])

            for _e in lst:
                if _e.course_id == cid:
                    lst.remove(_e)
                    self.count_course[cid] += -1
                    return

            raise EnrollmentNotFoundException

    def avg_mark(self, student_id):
        lst = self.enrollments.get(student_id, [])
        if not lst:
            return

        return round(sum(e.mark for e in lst) / len(lst), 2)

    def get_courses_of_student(self, sid):
        return self.enrollments.get(sid, [])

    def save(self, path=None):
        path = path or EnrollmentManager._ENROLL_PATH
        rows = []
        for _, lst in self.enrollments.items():
            for e in lst:
                rows.append(e.to_row())
        file_handler.write_csv(str(path), EnrollmentManager.EnrollFields._fields, rows)

    def load(self, path=None):
        path = path or EnrollmentManager._ENROLL_PATH
        rows = file_handler.read_csv(str(path), EnrollmentManager.EnrollFields._fields)
        rows = [Enrollment(**r) for r in rows]
        for r in rows:
            self.enroll(r, save_history=False)
