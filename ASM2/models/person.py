import datetime
from models.exceptions import InvalidDateException, InvalidEmailException


class Person:

    def __init__(self, sid, name, dob, email):
        self.sid = sid
        self.name = name
        self.dob = dob
        self.email = email

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
        try:
            _ = datetime.datetime.strptime(value, fmt)
        except Exception:
            raise InvalidDateException(
                f"Invalid date format should be: {value} (%Y-%m-%d)"
            )
        self._dob = value

    @email.setter
    def email(self, value):
        _val = str(value).lower()
        if "@" not in _val or "." not in _val:
            raise InvalidEmailException(f"Invalid email format {_val}")
        self._email = _val

    def to_row(self):
        return [self._sid, self._name, self._dob, self._email]

    # Dunder Method #

    def __str__(self):
        return f"{self._sid}, {self._name}"

    def __repr__(self):
        return f"Person(sid={self._sid}, name={self._name}, email={self._email}, dob={self._dob})"
