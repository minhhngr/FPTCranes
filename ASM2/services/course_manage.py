from collections import namedtuple

from common.config import ProjectPath
from utils import file_handler
from models.exceptions import CourseNotFoundException
from models import course


class CourseManager:
    _CoursePath = ProjectPath.DATA_PATH / "course_example.csv"
    _CourseFields = namedtuple("CourseFields", ["id", "name", "credit"])

    def __init__(self):
        self.courses = {}

    def add(self, course: course.Course):
        self.courses[course.course_id] = course

    def update(self, cid, **kwargs):
        if cid not in self.courses:
            raise CourseNotFoundException(cid)

        for k, v in kwargs.items():
            setattr(self.courses[cid], k, v)

    def search_by_credit(self, credit):
        return [c for c in self.courses.values() if c.credit == credit]

    def search_by_keyword(self, kw):
        return [c for c in self.courses.values() if kw.lower() in c.name.lower()]

    def save(self, path=None):
        path = path or CourseManager._CoursePath
        file_handler.write_csv(
            str(path),
            CourseManager._CourseFields._fields,
            (c for c in self.course.values()),
        )

    def load(self, path):
        path = path or CourseManager._CoursePath
        file_handler.read_csv(
            str(path),
            CourseManager._CourseFields._fields,
            (c for c in self.course.values()),
        )

    # def create(self):
    #     pass

    # def read(self):
    #     pass

    # def update(self):
    #     pass

    # def delete(self):
    #     pass

    # def search(self):
    #     pass

    # def search_credit(self):
    #     pass

    # def save(self):
    #     pass
