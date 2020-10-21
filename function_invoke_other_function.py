def greet(person, first_Time=False):
    if first_Time:
        return "Welcome for the first time, " + person + "!"
    return "Hello " + person

def greet_all(people):
    for person in people:
        print(greet(person,True))
friends=["Bob","Josh","Austin"]
greet_all(friends)