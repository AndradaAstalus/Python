languages = ["C++", "Java", "Python","Javascript","Python","Python"]

print("What are you searching for?")

lang= input()
found= False
for language in languages:
     if language == lang:
         print(language + " was found")
         found=True
         #break
#else:
     #print("Not found")
if not found:
    print(not found)
    print("Not found")
