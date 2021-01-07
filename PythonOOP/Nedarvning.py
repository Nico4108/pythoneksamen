from PythonOOP import inst


class People:
    description = "Normal Person"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print("My name is {} and i am {} years old".format(self.name, self.age))

    def eat(self, food):
        print("{} eats {}".format(self.name, food))

    def action(self):
        print("{} jumps".format(self.name))


class Baby(People):
    description = "baby"

    def talk(self):
        print("bibbob")

    def nap(self):
        print("{} takes a nap".format(self.name))


person = People("Jamal", 24)
person.talk()
person.eat("pasta")
person.action()

baby = Baby("Freja", 1)
baby.talk()
baby.action()

print(People.description)
print(Baby.description)

print(isinstance(baby, People))
print(isinstance(People, object))
print(isinstance(baby, object))


'''class Gender:
    def __init__(self, s):
        self.sex = s


class Student(inst.Instructor, Gender):  # nedarvning, du kan godt arve fra flere klasser
    def __init__(self, *args):
        inst.Instructor.__init__(self, args[0])  # self er objektet, hvis vi ikke skriver self, så følger objektet ikke med
        Gender.__init__(self, args[1])
        self.salary = args[2]


student = Student('Mads', 'male', 12000)
print(student.name, student.salary, student.sex)'''
