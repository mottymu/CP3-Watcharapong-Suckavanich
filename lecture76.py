# Set Function Example

fruits = {"apple", "banana", "pineapple", "orange"}

print(fruits)

fruits.remove("banana")

print(fruits)

fruits.add("grape")

print(fruits)

fruits.add("grape")

print(fruits)

fruits.clear()

print(fruits)

# Example 
userInput = int(input("Enter Number of Your Favorite Fruits : "))
myFruits = set()
while(len(myFruits)<userInput):
    myFruits.add(input("Fruits : "))
    print(myFruits)