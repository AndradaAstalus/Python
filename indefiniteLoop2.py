"""while True:
    print("Continue? Y/N")
    response=input()
    if response !="y" and response !="Y":
        break"""

while True:
    print("Continue?Y/N")
    response=input()
    if response.islower():
        print("It's lowercase")
    #if response == "Y" or response =='y':
    if response.lower() != "y":
        break
