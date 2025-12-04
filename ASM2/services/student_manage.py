from utils import file_handler
from common.config import ProjectPath

from collections import Counter, defaultdict, namedtuple
from typing import OrderedDict
import heapq
from models.exceptions import DuplicateStudentException, StudentNotFoundException
from models.student import Student


class StudentManager:
    _StudentFields = namedtuple(
        "StudentFields", ("sid", "name", "dob", "email", "major", "year", "gpa")
    )
    STUDENT_PATH = ProjectPath.DATA_PATH / "example.csv"

    def __init__(self):
        self.students = OrderedDict()
        self.by_years = defaultdict(list)
        self.count_major = Counter()
        self.min_gpa = []  # (gpa, sid)
        self.max_gpa = []  # (-gpa, sid)

    def _is_student_invalid(self, sid):
        if sid not in self.students:
            raise StudentNotFoundException(sid)

    def search_by_name(self, keyword):
        keyword = keyword.lower()

        result = (
            s.to_row() for s in self.students.values() if keyword in s.name.lower()
        )
        return list(result)

    def add(self, student: Student):
        if student.sid in self.students:
            raise DuplicateStudentException(student.sid)

        self.students[student.sid] = student
        self.by_years[student.year].append(student)
        self.count_major[student.major] += 1

        heapq.heappush(self.min_gpa, (student.gpa, student.sid))
        heapq.heappush(self.max_gpa, (-student.gpa, student.sid))

    def update(self, sid, *, student: Student):
        self._is_student_invalid(sid)
        stud = self.students[sid]
        vars_student = vars(student)
        for k, v in vars_student.items():
            setattr(stud, k, v)

    def remove(self, sid):
        self._is_student_invalid(sid)

        studs = self.students.pop(sid)
        self.by_years[studs.year].remove(studs)
        self.count_major -= 1

    def save(self, path=None):
        path = path or StudentManager.STUDENT_PATH
        file_handler.write_csv(
            str(path),
            StudentManager._StudentFields._fields,
            (s.to_row() for s in self.students.values()),
        )

    def load(self, path=None):
        path = path or StudentManager.STUDENT_PATH
        rows = file_handler.read_csv(path, StudentManager._StudentFields._fields)
        for row in rows:
            try:
                row_field = StudentManager._StudentFields(**row)
                s = Student(
                    row_field.sid,
                    row_field.name,
                    row_field.dob,
                    row_field.email,
                    row_field.major,
                    row_field.year,
                    row_field.gpa,
                )
                self.add(s)
            except Exception as e:
                print(f"[WARN] Skip bad row: {e}")

    def count(self):
        pass

    def top_n(self):
        pass
