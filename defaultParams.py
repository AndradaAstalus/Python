"""def greet(name='User'):
    if name == "Andra":
        return "Who do you think you are?"
    return "Hey, welcome, " + name

print(greet("Barbara"))
print(greet())"""

def greet(name='User', /,*, be_nice=True):
    if not be_nice:
        return "Who do you think you are?" + name
    return "Hey there! Welcome, " + name

print(greet("Andra",be_nice=False))
print(greet("Barbara",be_nice=True))
print(greet())
print(greet(be_nice=False))
print(greet(be_nice=False))