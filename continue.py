languages=["C++", "Java", "Python", "Javascript", "Python", "Python"]
print("What are you searching for?")
lang= input()
for language in languages:
    if language == lang:
        print("We found "+ lang)
        #continue
    else:    
        print(language + "not what we are looking for...")

