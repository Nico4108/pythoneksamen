# Model an organisation of employees, management and board of directors in 3 sets.
boardOfDiretors = {"Benny", "Hans", "Tine", "Mille", "Torben", "Troels", "Søren"}
managers = {"Tine", "Trunte", "Rane"}
employees = {"Niels", "Anna", "Tine", "Ole", "Trunte", "Bent", "Rane", "Allan", "Stine", "Claus", "James", "Lars"}

# who in the board of directors is not an employee?
set4 = boardOfDiretors.difference(employees)
print(set4)

# who in the board of directors is also an employee?
set5 = boardOfDiretors.intersection(employees)
print(set5)

# how many of the management is also member of the board?
set6 = managers.intersection(boardOfDiretors)
print(set6)

# All members of the managent also an employee
set7 = managers.isdisjoint(employees)
set71 = managers.intersection(employees)
print(set7, set71)

# All members of the management also in the board?
set8 = managers.isdisjoint(boardOfDiretors)
set81 = managers.intersection(boardOfDiretors)
print(set8, set81)

# Who is an employee, member of the management, and a member of the board?
set9 = employees.intersection(boardOfDiretors, managers)
print(set9)

# Who of the employee is neither a memeber or the board or management?
set10 = employees.difference(managers, boardOfDiretors)
print(set10)


# Set Comprehension
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

sentence = "The cat in the hat had two sidekicks, thing one and thing two."
words = sentence.lower().replace('.', '').replace(',', '').split()
unique_words = {word for word in words}
print(unique_words)
