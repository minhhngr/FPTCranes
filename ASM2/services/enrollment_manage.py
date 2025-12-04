from collections import Counter, deque, namedtuple

from common.config import ProjectPath
from utils import file_handler


class EnrollmentManager:
    _EnrollPath = ProjectPath.DATA_PATH / "enroll_example.csv"
    _EnrollFields = namedtuple("EnrollFields", ("student_id", "course_id", "mark"))

    def __init__(self):
        self.enrollments = {}
        self.history = deque()
        self.count_course = Counter()

    def save(self, path=None):
        path = path or EnrollmentManager._EnrollPath
        rows = []
        for _, lst in self.enrollments.items():
            for e in lst:
                rows.append(e.to_row())
        file_handler.write_csv(str(path), EnrollmentManager._EnrollFields._fields, rows)

    def load(self, path=None):
        path = path or EnrollmentManager._EnrollPath
        rows = file_handler.read_csv(str(path), EnrollmentManager._EnrollFields._fields)
        for r in rows:
            self.enroll(r.student_id, r.course_id, r.mark, save_history=False)

    def undo_enroll(self):
        pass

    def update(self):
        pass

    def update_score(self):
        pass

    def count(self):
        pass

    def show(self):
        pass
