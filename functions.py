"""def greet(name):
    if name == "Andra":
        print("go to PT")
        #return
    #print("Hey there!")
    #print("Welcome, " + name + "!")    
    else:    
         print("Hey there!")
         print("Welcome, " + name + "!")"""

def greet(name):
    if name == "Andra":
        return "Who do you think you are?"
    return "Hey, welcome, " + name
returned=greet("Andra")
print(returned)
 
 

greet("Barbara")
greet("Andra")