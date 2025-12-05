from models.exceptions import InvalidMarkException


class Enrollment:

    def __init__(self, student_id, course_id, mark):
        self.student_id = student_id
        self.course_id = course_id

        try:
            mark = float(mark)
            if not (0 <= mark <= 10):
                raise InvalidMarkException(mark)
            self.mark = mark
        except Exception:
            raise ValueError(mark)

    def to_row(self):
        return [self._student_id, self._course_id, self._mark]
