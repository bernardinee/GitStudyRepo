class Person:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name


class Student(Person):
    def __init__(self, first_name, last_name,hall_of_residence,courses=None):
        self.hall_of_residence=hall_of_residence
        self.courses=courses

    
    