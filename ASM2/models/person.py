from ASM2.models.exceptions import InvalidDateException, InvalidEmailException


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
    def set_sid(self, value):
        self._sid = value

    @name.setter
    def set_name(self, value):
        self._name = value

    @dob.setter
    def set_dob(self, value):
        if not value:
            raise InvalidDateException
        self._dob = value

    @email.setter
    def set_email(self, value):
        if not value:
            raise InvalidEmailException
        self._email = value
    
    def to_row(self):
        return [self.sid, self.name, self.dob, self.email]

    # Dunder Method #

    def __str__(self):
        pass

    def __repr__(self):
        pass
    