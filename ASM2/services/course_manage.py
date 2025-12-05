from collections import namedtuple

from common.config import ProjectPath
from utils import file_handler
from models.exceptions import CourseNotFoundException
from models.course import Course


class CourseManager:
    _COURSE_PATH = ProjectPath.DATA_PATH / "courses.csv"
    CourseFields = namedtuple("CourseFields", ["course_id", "name", "credit"])

    def __init__(self):
        self.courses = {}

    def show(self):
        if not self.courses:
            print("Courses is empty")

        for courses in self.courses.values():
            print(repr(courses))

    def add(self, course: Course):
        self.courses[course.course_id] = course

    def update(self, cid, **kwargs):
        if cid not in self.courses:
            raise CourseNotFoundException(cid)

        for k, v in kwargs.items():
            setattr(self.courses[cid], k, v)

    def remove(self):
        pass

    def search_by_credit(self, credit):
        return [c for c in self.courses.values() if c.credit == credit]

    def search_by_keyword(self, kw):
        return [c for c in self.courses.values() if kw.lower() in c.name.lower()]

    def load(self, path=None):
        path = path or CourseManager._COURSE_PATH
        rows = file_handler.read_csv(
            str(path),
            CourseManager.CourseFields._fields,
        )
        for r in rows:
            course = Course(**r)
            self.add(course)

    def save(self, path=None):
        path = path or CourseManager._COURSE_PATH
        file_handler.write_csv(
            str(path),
            CourseManager.CourseFields._fields,
            (c.to_row() for c in self.courses.values()),
        )
