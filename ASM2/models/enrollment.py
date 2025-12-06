from models.exceptions import InvalidMarkException


class Enrollment:

    def __init__(self, student_id=None, course_id=None, mark=0.0):
        self.student_id = student_id
        self.course_id = course_id
        self.mark = mark

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):
        self._student_id = value

    @property
    def course_id(self):
        return self._course_id

    @course_id.setter
    def course_id(self, value):
        self._course_id = value

    @property
    def mark(self):
        return self._mark

    @mark.setter
    def mark(self, value):
        try:
            value = float(value)
            if not (0 <= value <= 10):
                raise InvalidMarkException(value)
            self._mark = value
        except Exception as e:
            print(e)

    def to_row(self):
        return [self._student_id, self._course_id, self._mark]

    def __str__(self):
        return f"{self._student_id}, {self._course_id}, {self._mark}"

    def __repr__(self):
        return f"Enrollment(student_id={self._student_id}, " f"course_id={self._course_id}, " f"mark={self._mark})"
