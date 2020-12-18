import modEksamen as me
import platform


y = platform.system()
print(y)

print(me.foo(['quux', 'corge', 'grault']))
print(me.a)
print(me.s)

# Web scrape
x = me.Foo.soup

# calculator
# x = me.Cal.choice

print(x)

