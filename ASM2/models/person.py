import datetime
from models.exceptions import InvalidDateException, InvalidEmailException


class Person:

    def __init__(self):
        self._sid = None
        self._name = None
        self._dob = None
        self._email = None

    @property
    def sid(self):
        return self._sid

    @property
    def email(self):
        return self._email

    @property
    def name(self):
        return self._name

    @property
    def dob(self):
        return self._dob

    @sid.setter
    def sid(self, value):
        self._sid = value

    @name.setter
    def name(self, value):
        self._name = value

    @dob.setter
    def dob(self, value):
        fmt = "%Y-%m-%d"
        ptime = datetime.datetime.strptime
        try:
            result = ptime(value, fmt)
        except:
            _ex = ptime("2004-05-12", fmt)
            raise InvalidDateException(f"Invalid date format should be: {_ex!r}")
        self._dob = value

    @email.setter
    def email(self, value):
        _val = str(value).lower()
        if "@" not in _val or "." not in _val:
            raise InvalidEmailException("Invalid email format")
        self._email = _val

    def to_row(self):
        return [self.sid, self.name, self.dob, self.email]

    # Dunder Method #

    def __str__(self):
        return f"{self.sid}, {self.name}"

    def __repr__(self):
        return f"Person(sid={self.sid}, name={self.name}, email{self.email}, dob={self.dob})"
