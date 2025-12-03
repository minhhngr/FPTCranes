from collections import Counter, defaultdict, namedtuple
from typing import OrderedDict
import heapq
from models.exceptions import DuplicateStudentException, StudentNotFoundException
from models.student import Student

rows = namedtuple("rows", ("id", "name", "dob", "email", "major", "year", "gpa"))


class StudentManager:

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
        pass

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

    def save(self):
        pass

    def load(self):
        pass

    def count(self):
        pass

    def top_n(self):
        pass
