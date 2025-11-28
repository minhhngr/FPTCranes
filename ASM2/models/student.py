from models.person import Person


class Student(Person):

    def __init__(self):
        super().__init__()
        self._major = None
        self._year = None
        self._gpa = None

    @property
    def major(self):
        return self._major

    @property
    def year(self):
        return self._year

    @property
    def gpa(self):
        return self._gpa

    @major.setter
    def major(self, value):
        self._major = value

    @year.setter
    def year(self, value):
        try:
            self._year = int(value)
        except Exception:
            raise ValueError("Years must be number")

    @gpa.setter
    def gpa(self, value):
        try:
            self._gpa = float(value)
        except Exception:
            raise ValueError("GPA must be number")

    def to_row(self):
        return [
            self.sid,
            self.name,
            self.dob,
            self.email,
            self.major,
            self.year,
            self.gpa,
        ]

    # Dunder Method #

    def __str__(self):
        return f"{self.sid}, {self.name}"

    def __repr__(self):
        return f"Person({self.to_row()})"
    
    def __lt__(self, other):
        return self.gpa < other.gpa

    def __gt__(self, other):
        return self.gpa > other.gpa
