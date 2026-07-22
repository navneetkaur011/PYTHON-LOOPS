print("Ques-1. Print numbers from 1 to 100")
Numbers = 1
while Numbers<=100:
    print(Numbers)
    Numbers += 1
print("Done!")

print("Ques-2. Print numbers from 100 to 1")
i = 100
while i>=1:
    print(i)
    i -= 1
print("Loop Ended!")

print("Ques-3. Print the multiplication table of number n")
n = int(input("Enter number: "))
i = 1
while i <= 10:
    print(n*i)
    i += 1
print("Done!")

print("Ques-4. Print the elements of the following list using a loop") 
List= ["Ironman", "Thor", "Superman", "Batman"]
i = 0
while i < len(List):
    print(List[i])
    i += 1

print("Ques-5. Search for a number x in the tuple using loop")
Tup = (12, 109, 67, 92, 34, 181, 27, 11, 567, 123, 34)
x = int(input("Enter number to search in a tuple: "))
i = 0
while i< len(Tup):
    if(Tup[i] == x):
       print("Found at Index", i)
    i += 1

print("Ques-6. Print the elements of the list using for loop.")
list = [12, 56, 38, 22, 90, 18, 29, 58, 11, 3]
for val in list:
    print(val)

print("Ques-7. Search for a number in the tuple using for loop")
Tup = (13, 34, 67, 20, 92, 44, 10, 45, 67, 59, 67, 92)
x = int(input("Enter number to search: "))
i = 0
for val in Tup:
    if(val == x):
        print("Found", x, "at index", i)
    i += 1

