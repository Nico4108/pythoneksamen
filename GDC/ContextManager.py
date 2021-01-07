from contextlib import contextmanager

# indbygget context manager (with)
with open('hello.txt', 'a') as f:
    f.write("Hello world my man123!\n")


# hvad "with" indeholder # SPØRG CLAUS D.11!!!!!!!!
class ManagedFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'a')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


with ManagedFile('hello.txt') as f:
    f.write("Hello world my man!\n")


# custom context manager
@contextmanager
def managed_file(name):
    try:
        f = open(name, 'a')
        yield f
    finally:
        f.close()


with managed_file('hello.txt') as f:
    f.write("What up!!\n")
    f.write("my doog")
