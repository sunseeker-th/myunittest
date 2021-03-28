"""Employeee class for unittest"""

class Employee(object):
    """ A sample Employee class"""

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        """ email """
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        """ fullname """
        return '{}.{}'.format(self.first, self.last)

    def apply_raise(self):
        """ apply raise """
        self.pay = int(self.pay * self.raise_amt)
