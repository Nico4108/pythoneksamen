# Uden function
print("Program starts")

print("Hi Peter")
print("Nice to see you again!")
print("Enjoy our video!")

# some lines of codes
the_answer = 42

print("Hi Sarah")
print("Nice to see you again!")
print("Enjoy our video!")

width, length = 3, 4
area = width * length

print("Hi Dominque")
print("Nice to see you again!")
print("Enjoy our video!")
print("-----------------------------------------")
# Med function

def greet(name):
    print("Hi " + name)
    print("Nice to see you again!")
    print("Enjoy our video!")


print("Program starts")

greet("Peter")

# some lines of codes
the_answerr = 42

greet("Sarah")

width, length = 3, 4
areaa = width * length

greet("Dominque")

print("----------------------------------")
# Methods skal have Self som parameter da den referer til en class eller object
class Person:
    species = 'human'

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    def speak(self, sound):
        return "{} siger {}".format(self.name, sound)

    def birthday(self):
        self.age+=1


nadia = Person(22, "Nadia")
thea = Person(24, "Thea")

print(thea.description())

print(nadia.speak("Bare Prov"))

thea.birthday()

print(thea.description())

print("{} is {} and {} is {}".format(nadia.name, nadia.age, thea.name, thea.age))

if thea.species == "human":
    print("{} is a {}".format(thea.name, thea.species))