# # collectionh = single "variable" used to stores multiple values
# # list = [] ordered and changeable. Duplicates OK
# # set = {} unordered and immutable
# # Tuple = () ordered and unchangeable

# fruits = ["apple", "orange", "banana", "coconut"]
# # print (fruits[0]) # to print one of the objects in the list you can put the number of the object (the first one being 0)
# # print(fruits[0:3]) # to get the first three elements
# # print(fruits[::2]) # for every 2 elements
# # print(fruits[::-1]) # to reverse

# # for fruit in fruits:
# #     print(fruit)

# # print(dir(fruits))
# # print(help(fruit)) # for a description of all the functions you can perform
# # print(len(fruits)) # counts how many elements you have

# # print("pineapple" in fruits) # tells you true or false

# # fruits[0] = "pineapple" #changes the element of the element in the number put in brackets
# # fruits.append("pineapple") # adds element to the end of the list
# # fruits.remove("apple") # removes element from list
# # fruits.insert(0, "pineapple") # to replace an element. 0 would replace the first element
# # fruits.sort() # sorts in alphabetical order
# # fruits.reverse() #only reversed in the order originally given
# # sort and then reverse to reverse in alphebetical order
# # fruits.clear() # to clear
# # print(fruits.index("apple")) # to find the number order of the element
# print(fruits)

cars = ["Ford", "Volvo", "BMW"]

for car in cars:
    requestcar = input("Enter a car: ")
    cars.append(requestcar)
    print(f"The car in the list area: {car}")
    if len(cars) > 10:
        print("You have reached the maximum number of cars")
        break