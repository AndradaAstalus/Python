languages=["C++","Java", "Python", "Javascript"]
print("What are you searching for?")
lang = input()
for language in languages:
    print(language)
    if language == lang:
        print("we found " + lang)
        break