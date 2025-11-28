from ASM2.models.person import Person


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
    def set_major(self, value):
        self._major = value

    @year.setter
    def set_year(self, value):
        self._year = value

    @gpa.setter
    def set_gpa(self, value):
        self._gpa = value

    def to_row(self):
        return [
            self.sid, self.name, self.dob, 
            self.email, self.major, self.year, self.gpa
        ]

    # Dunder Method #

    def __lt__(self):
        pass

    def __gt__(self):
        pass
