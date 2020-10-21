age= 31
fun = False
likes_to_Dance=False
"""if (age < 30 or fun) and likes_to_Dance:
    print("You're invited")
else:
    print("You're not on the list")"""

if (age < 30 or fun):
    if likes_to_Dance:
        print("You're invited")
    else:
        print("Oh no! You can't dance?")
else:
    print("You are not invited")
