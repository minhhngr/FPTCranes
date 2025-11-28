from ASM2.models.exceptions import InvalidMarkException


class Enrollment:
    
    def __init__(self):
        self._student_id = None
        self._course_id = None
        self._mark = None

    @property
    def student_id(self):
        return self._student_id

    @property
    def course_id(self):
        return self._course_id

    @property
    def mark(self):
        return self._mark

    @mark.setter
    def set_mark(self, value):
        if 0 > value > 10:
            raise InvalidMarkException()
        self._mark = value
    
    def to_row(self):
        return [self._student_id, self._course_id, self._mark]
