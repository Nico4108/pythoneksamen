class Deck:
    def __init__(self):
        self.cards = ['A', 'K', 4, 7]

    # __len__ er en instance method
    def __len__(self):
        # len() er build in fuction, ikke afhængig af objektet.
        return len(self.cards)

    def __getitem__(self, x):
        return self.cards[x]

    def __add__(self, n):
        # .append() er build in method, afhængig af objektet cards.
        return self.cards.append(n)

    # laver cards til en dict
    # en instance method der bruger en build in function
    # som bruger en instance method.
    # __Repr__ gør det readable
    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        return f'Cards: {self.cards}'

    def __setitem__(self, key, value):
        self.cards[key] = value

    def __delitem__(self, key):
        del(self.cards[key])


d = Deck()
print(len(d))  # __len__ 5
print(d[1])  # __getitem__ 9
print(d+"hey", d.cards)  # __add__ 12
print(repr(d))  # __repr__ 17
print(str(d.cards))  # __str__ 20
d[2] = 1000
print(d)  # __setitem__
del(d[1])
print(d)  # __delitem__
