"""def greet_all(people):
    for person in people:
        print("hello " + person)
friends=["Bob","Josh", "Austin"]
greet_all(friends)"""

def greet_all(*people):
    for person in people:
        print("Hello " + person)
greet_all("Bob","Josh","Austin")
