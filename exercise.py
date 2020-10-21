import math
import copy
age=15
age_str=str(age)
id_age_str=id(age_str)
other= math.floor(2.6)
added=id_age_str + other
added_str=str(added)
length=len(added_str)
#print(length)
#print(len(str(id(str(age))+math.floor(2.6))))
#print("Your message is "+ str(len(msg))+ " characters long")
#print("Your message is", str(len(msg)), "characters long")
ages=[12,18,28]
people=["Caleb", "Sabrina", "emily"]
my_fav_things=["working out", 7, ["amazon prime", 'netflix']]
my_fav_things=["walking","dancing",7]
my_fav_things[0]=["jogging"]
#print(len(my_fav_things))
#print(my_fav_things)
my_favs2=["working out", 7,['amazon prime', ['netfix','hulu']]]
#copy=my_favs2[:]
DeepCopy=copy.deepcopy(my_favs2)
#copy=my_favs2.copy() #another way of copying
#print(copy)
DeepCopy[2][0]="cinemax"
print(my_favs2,DeepCopy)
