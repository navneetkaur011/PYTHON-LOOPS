print("---FOR LOOP---")
Emotions = ["Funny", "Sad", "chill", "Rude", "Happy", "Kind"]
for el in Emotions:
    print(el)

Veggies = ("potato", "tomato", "Cucumber", "Eggplant", "Ladyfinger")
x = str(input("\nEnter veggie:"))
for el in Veggies:
    if(el == x):
        print("Found!")
        break
    print(el)
else:
    print("Not Found!\n")

""" 
RANGE: Range function returns a sequence of numbers , starting from 0 by default and increments 
       by 1 (by default) and stops before a specified number.
"""
print("---Range function---")
for i in range(11):
    print(i)
print()

for i in range(2,10,2):   #range(start,stop,step)
    print(i)

# PASS: It is a null statement that does nothing. It is used as a placefolder for future code. 
print("\n---Pass statement---")
for i in range(0,39,-2):
    pass
print("This block is currently empty as a placeholder for future code")

