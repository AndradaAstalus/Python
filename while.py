"""i=10
while i > 0:
    print(i)
    i-=5"""

"""i=0
while i<10:
    print(i)
    i+=1

for i in range(0,10,1):
    print(i)"""

numbers=[5,3,6,7,4,2,4,3]
i=0
square=500
success= False
while i < len(numbers):
    if numbers[i] ** 2 > square:
        print(numbers[i], "squared is larger than " ,square)
        success=True
        break
    print(numbers[i], "squared is not larger than", square)
    i+=1
#else:
    #print("none squared are larger than", square)
if not success:
    print("none were large enough")