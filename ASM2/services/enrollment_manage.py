from collections import Counter, deque, namedtuple

from models.enrollment import Enrollment
from models.exceptions import EnrollmentNotFoundException
from common.config import ProjectPath
from utils import file_handler


class EnrollmentManager:
    _ENROLL_PATH = ProjectPath.DATA_PATH / "enrollments.csv"
    _EnrollFields = namedtuple("EnrollFields", ("student_id", "course_id", "mark"))

    def __init__(self):
        self.enrollments = {}
        self.history = deque()
        self.count_course = Counter()

    def get_courses_of_student(self, sid):
        return self.enrollments.get(sid, [])

    def enroll(self, sid, cid, mark, save_history=True):
        e = Enrollment(sid, cid, mark)
        self.enrollments.setdefault(sid, []).append(e)
        self.count_course[cid] += 1

        if save_history:
            self.history.append(("add", sid, cid))

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

    def save(self, path=None):
        path = path or EnrollmentManager._ENROLL_PATH
        rows = []
        for _, lst in self.enrollments.items():
            for e in lst:
                rows.append(e.to_row())
        file_handler.write_csv(str(path), EnrollmentManager._EnrollFields._fields, rows)

    def load(self, path=None):
        path = path or EnrollmentManager._ENROLL_PATH
        rows = file_handler.read_csv(str(path), EnrollmentManager._EnrollFields._fields)
        rows = [EnrollmentManager._EnrollFields(**r) for r in rows]
        for r in rows:
            self.enroll(r.student_id, r.course_id, r.mark, save_history=False)
