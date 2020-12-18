from PythonOOP import inst


class Gender:
    def __init__(self, s):
        self.sex = s


class Student(inst.Instructor, Gender): # nedarvning, du kan godt arve fra flere klasser
    def __init__(self, *args):
        # super().__init__(args[0]) # super tager objektet med over
        inst.Instructor.__init__(self, args[0]) # self er objektet, hvis vi ikke skriver self, så følger objektet ikke med
        Gender.__init__(self, args[1])
        self.salary = args[2]


student = Student('Mads', "male", 12000)
print(student.name, student.salary, student.sex)