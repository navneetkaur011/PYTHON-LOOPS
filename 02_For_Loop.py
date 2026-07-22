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
    print("Not Found!")