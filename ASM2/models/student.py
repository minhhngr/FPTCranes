from models.person import Person


class Student(Person):

    def __init__(
        self,
        sid=None,
        name=None,
        dob="1900-01-01",
        email="example@org.com",
        major=None,
        year=1900,
        gpa=0.0,
    ):
        super().__init__(sid=sid, name=name, dob=dob, email=email)
        self.major = major
        self.year = year
        self.gpa = gpa

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
            self._sid,
            self._name,
            self._dob,
            self._email,
            self._major,
            self._year,
            self._gpa,
        ]

    # Dunder Method #

    def __str__(self):
        return f"{self._sid}, {self._name}"

    def __repr__(self):
        return f"Person({self.to_row()})"

    def __lt__(self, other):
        return self._gpa < other.gpa

    def __gt__(self, other):
        return self._gpa > other.gpa
