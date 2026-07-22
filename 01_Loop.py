# Loops are used to repeat instructions.
i = 1
while i<=10:
    print("Good Vibes")
    i+=1
print("----Loop Ended!----") 

# A simple while loop countdown
print("\nCountdown:")
countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Done!")

# BREAK: used to terminate the loop when encountered 
List = (12, 24, 56, 90, 43, 102, 109, 231)
x = int(input("Enter number to find: "))
i = 0
while i < len(List):
    if(List[i] == x):
        print("Found at index", i)
        break
    else:
        print("Finding....")
    i += 1
print("End of loop")

# CONTINUE: Terminates execution in the current iteration & continues of the loop with the next iteration
List = (21, 45, 62, 98, 40, 102, 37, 22)
x = int(input("Enter number:"))   
i = 0 
while i < len(List):
    if(List[i] == x): 
        i += 1 
        continue #skip
    print(List[i])
    i += 1 