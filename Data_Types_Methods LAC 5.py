# Python Lecture – Methods of Data Types
# 1. Introduction to Methods
# Methods are built-in functions attached to objects.

# પદ્ધતિઓ એ ઑબ્જેક્ટ્સ સાથે જોડાયેલા બિલ્ટ-ઇન ફંક્શન્સ છે.

# તેઓ ડેટા પ્રકારો પર કામગીરી કરવામાં મદદ કરે છે.

# They help perform operations on data types.

# Syntax:

# object.method()
# Example:

# name = "python"
# print(name.upper())

# Here:
# name → object
# upper() → method






# 2. Methods in String (str)
# Strings are immutable sequences of characters.

# Common String Methods
# Method	Purpose
# upper()	Convert to uppercase
# lower()	Convert to lowercase
# title()	First letter capital
# capitalize()	Capitalize first character
# strip()	Remove spaces
# replace()	Replace text
# split()	Convert string into list
# join()	Join list into string
# find()	Find position
# count()	Count occurrences
# startswith()	Check starting
# endswith()	Check ending
# isdigit()	Check digits
# isalpha()	Check alphabets

# 3. upper()
# name = "mustafa"
# print (name.upper())

# 4. lower()
# text = "MUSTAFA"
# print (text.lower())

# 5. title()
# Capitalizes first letter of every word.

# Example:

# name = "python programming"
# print(name.title())

# 6. capitalize()
# Capitalizes only first character.

# Example:

# text = "python"
# print(text.capitalize())

# 7. strip()
# Removes extra spaces.

# Example:

# text = "   Python   "
# print(text.strip())

# 8. replace()
# Replaces text.

# Example:

# text = "I like Java"
# print(text.replace("Java", "Python"))

# 9. split()
# Converts string into list.

# Example:
# data = " komal   nilam    surekha"
# print(data.split())

# 10. join()
# Joins list into string.

# skills = ["Python", "SQL", "PowerBI"]
# print(" @ ".join(skills))

# 11. find()
# Returns position of character/word. (LIKE INDEX NUMBER)

# Example:
# text = "Python"
# print(text.find("h"))

# 12. count()
# Counts occurrences. (count letters in sentence)

# Example:
# text = "python programming is a wonderful langauge"
# print(text.count("f"))

# 13. startswith() and endswith()

# startswith()
# text = "Python"
# print(text.startswith("Py"))

# endswith()
# text = "Python"
# print(text.endswith("on"))

# 14. isdigit()
# Checks whether string contains digits only.

# num = "12345"
# print(num.isdigit())

# 15. isalpha()

# name = "Python"
# print(name.isalpha())






# 16. List Methods (list)
# Lists are mutable ordered collections.

# Common List Methods
# Method	Purpose
# append()	Add item
# extend()	Add multiple items
# insert()	Insert at position
# remove()	Remove item
# pop()	Remove by index
# clear()	Remove all items
# index()	Find position
# count()	Count values
# sort()	Sort list
# reverse()	Reverse list
# copy()	Copy list

# 17. append()
# Adds single item at end.

# Example:
# fruits = ["Apple", "Banana"]
# fruits.append("Mango")
# print(fruits)

# 18. extend()
# Adds multiple items.

# Example:
# numbers = [1,2]
# numbers.extend([3,4,5])
# print(numbers)

# 19. insert()
# Insert item at specific position. (index number thi sharp position ma new item add kari sakay.)

# Example:
# names = ["Rahul", "Amit", "Nimit", "lakhya"]
# names.insert(3, "Harshil")
# print(names)

# 20. remove()
# Removes specific item. (remove item by specific mention item name)

# Example:
# fruits = ["Apple", "Banana"]
# fruits.remove("Apple")
# print(fruits)

# 21. pop()
# Removes item using index.

# Example:
# numbers = [10,20,30]
# numbers.pop(1)
# print(numbers)

# 22. clear()
# Removes all items.

# Example:
# data = [1,2,3]
# data.clear()
# print(data)

# 23. index()
# Returns position of item. (perticular koi ak item ni index number sodhi ape che.)

# Example:
# names = ["A", "B", "C"]
# print(names.index("B"))

# 24. count()
# Counts occurrences. (count specific item in list)

# Example:
# numbers = [1,1,2,3,1,1]
# print(numbers.count(1))

# 25. sort()
# Sorts list.

# Example:
# numbers = [5,2,8,1]
# numbers.sort()
# print(numbers)

# 26. reverse()
# Reverses list.

# Example:
# numbers = [1,2,3]
# numbers.reverse()
# print(numbers)

# Output: [3,2,1]

# 27. copy()
# Copies list.

# Example:

# a = [1,2,3]
# b = a.copy()
# print(b)





# 28. Tuple Methods (tuple)
# Tuple is immutable.

# Only two important methods:

# Method	Purpose
# count()	Count values
# index()	Find position

# (1) count()
# data = (1,1,2,3)
# # print(data.count(1))

# # (2) index()
# data = (1,1,2,3)
# print(data.index(2))




# 29. Set Methods (set)
# Sets store unique unordered values.

# Common Set Methods
# Method	        Purpose
# add()	        Add item
# update()	    Add multiple items
# remove()	    Remove item
# discard()	    Remove safely
# pop()	        Remove random item
# clear()	        Remove all
# union()	        Combine sets
# intersection()	Common values
# difference()	Unique values


# 30. add()
# numbers = {1,2,3}
# numbers.add(4)
# print(numbers)

# 31. update()
# numbers = {1,2,3}
# numbers.update([5,6])
# print(numbers)

# 32. remove() vs discard()
# remove()
# Gives error if value not found.
# numbers = {1,2,3,4,5,6,7,8}
# numbers.remove(5)


# discard()
# Does not give error.
# numbers = {1,2,3,4,5,6,7,8}
# numbers.discard(4)

# W3  POP
# Remove a random item from the set:
# fruits = {"apple", "banana", "cherry"}
# fruits.pop() 
# print(fruits)

# W3 CLEAR
# Remove all elements from the fruits set:
# fruits = {"apple", "banana", "cherry"}
# fruits.clear()
# print(fruits)

# 33. union()
# Combines sets.

# Example:
# a = {1,2}
# b = {2,3}
#     print(a.union(b))

# 34. intersection()
# Findout Common values only.

# Example:
# a = {1,2}
# b = {2,3}
# print(a.intersection(b))

# W3 difference
# Return a set that contains the items that only exist in set x, and not in set y:

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.difference(y)
# print(z)











# 35. Dictionary Methods (dict)
# Dictionaries store key-value pairs.

# Common   Dictionary Methods
# Method	 Purpose
# keys()	 Get keys
# values() Get values
# items()	 Get key-value pairs
# get()	 Get value safely
# update() Update dictionary
# pop()	 Remove item
# clear()	 Remove all
# copy()	 Copy dictionary


# 36. keys()
# Get keys
# student = {
#     "name": "Rahul",
#     "age": 21
# } 
# print(student.keys())

# 37. values()
# Get values
# student = {
#     "name": "Rahul",
#     "age": 21
# }
# print(student.values())

# 38. items()
# Get key-value pairs
# student = {
#     "name": "Rahul",
#     "age": 21
# }
# print(student.items())

# 39. get()
# Safe way to access values.

# Example:
# student = {
#     "name": "Rahul",
#     "age": 21
# }
# print(student.get("name"))

# Difference Between [] and get()
# print(student["marks"])
# Gives error if key missing.

# But:

# print(student.get("marks"))
# Output:

# None

# 40. update()
# Updates dictionary.

# Example:
# student = {
# "name": "Rahul",
# "age": 21
# }
# student.update({"city":"Ahmedabad"})
# print(student)

# 41. pop()
# Removes key.

# Example:
# student = {
# "name": "Rahul",
# "age": 21
# }
# student.pop("age")
# print(student)

# w3 clear()
# Remove all elements from the car dictionary:

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car.clear()
# print(car)

# w3 copy()
# Copy the car dictionary:

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = car.copy()
# print(x)

# 42. Practical Real-Life Example Of Update In Dictionary
employee = {
    "name": "Chetan",
    "skills": ["Python", "SQL"],
    "salary": 35000
}

employee["skills"].append("Power BI")

print(employee)


43. Common Beginner Mistakes
Mistake	                            Problem
Using append() on string	         Error
Using sort() on mixed data types   	 Error
Using remove() for missing set value Error
Forgetting list is mutable	    Unexpected changes



44. Practice Questions
Q1 Convert string into uppercase.

Q2 Split sentence into words.

Q3 Add 5 values into list using append().

Q4 Sort list in descending order.

Q5 Create dictionary and print keys & values.


45. Interview Questions
Difference between append() and extend()?
Difference between remove() and pop()?
Why tuple has fewer methods?
Difference between discard() and remove()?
Why use get() in dictionary?


46. Final Summary
Data Type	Common Methods
String	   upper(), split(), replace()
List	   append(), sort(), remove()
Tuple	   count(), index()
Set	add(), union(), intersection()
Dictionary keys(), values(), items()
