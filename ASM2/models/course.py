class Course:

    def __init__(self, course_id, name, credit):
        self.course_id = course_id
        self.name = name
        self.credit = credit

    def to_row(self):
        return [self.course_id, self.name, self.credit]

    # Dunder Method #

    def __str__(self):
        return f"{self.course_id} - {self.name}"

    def __repr__(self):
        return f"Course(course_id={self.course_id}, name={self.name}, credit={self.credit})"
