favorite_animal = 'dog'

student = {
    'name': 'Maria',
    'favorite_integer': 5,
    favorite_animal: 'llama' # notice the lack of quotes around favorite_animal
}

print(student)
# prints: {'name': 'Maria', 'favorite_integer': 5, 'dog': 'llama'}
# note the 'dog' key - the value of the favorite_animal variable is used

# We use square brackets to get an item’s value:
name = student['name']
print(name)
# prints: Maria

# When attempting to access a key that does not exist in a dictionary, a KeyError will be raised.
# One option to avoid this error is to use the get method:
# favorite_food = student['favorite_food']
# error: KeyError: 'favorite_food'

print(student.get('favorite_food'))
# prints: None

# Another way to avoid the KeyError is to use the in operator to check if the dictionary includes a key:
if 'course' in student:
    print(f"{student['name']} is enrolled in {student['course']}")
else:
    print(f"{student['name']} is not enrolled in a course")
    # prints: Maria is not enrolled in a course

# We not only use square brackets to get an item’s value - we also use it to set an item’s value:
student['name'] = 'Mariana'
print(student['name'])
# prints: Mariana

# Assigning to a key that does not exist will create a new item in the dictionary.
# Let’s add an item to the student dictionary:
student['age'] = 25

# The del statement is used to delete an item from a dictionary:
del student['dog']
# verify that the item was deleted
print('dog' in student)
# prints: False

# Use the built-in len function to retrieve the number of items in a dictionary:
print(student)
# prints: {'name': 'Maria', 'favorite_integer': 5, 'age': 25}
print(len(student))
# prints: 3
print(len({}))
# prints: 0

# for loops are used to iterate over the items in a dictionary.
# However, accessing the value of an item as follows is considered to be a Python anti-pattern:
for key in student:
    print(f"{key} is {student[key]}")
    # prints:
    # name is Maria
    # favorite_integer is 5
    # age is 25

# Modifying a dictionary using this approach can lead to potential issues, which is why this is not preferred.
# The preferred approach is to use the items() method to obtain a dictionary view object.
# Use it in a for in loop to iterate over the view object:
for key, val in student.items():
    print(f"{key} is {val}")
    # prints:
    # name is Maria
    # favorite_integer is 5
    # age is 25


# Define a Python dictionary named where_my_things_are containing a few items where:
#     the keys are things you have
#     the values are the locations where you keep those things
# Write a for loop that iterates over the items in the dictionary and prints each one as:
#     My [thing] is kept [location]

where_my_things_are = {
    "laptop": "desk",
    "gum": "drawer",
    "backpack": "closet",
    "award": "cabinet"
}

# Print each item in the specified format
for thing, location in where_my_things_are.items():
    print(f"My {thing} is kept in my {location}")

colors = ['red', 'green', 'blue']
# Accessing the individual items of a list is much like accessing elements in a JavaScript array. 
# Use square brackets with an expression that evaluates to an integer to access the element at that index:
print(colors[0])
# prints: red

# However, unlike in JavaScript, we can use negative integers to index from the end of a list:
print(colors[-1])
# prints: blue

# We also use square brackets to target an item of a list for assignment:
colors[-1] = 'brown'
print(colors)
# prints: ['red', 'green', 'brown']

# Unlike with JavaScript arrays, assigning to a non-existing index results in an error:
# colors[10] = 'yellow'
# # error: IndexError: list assignment index out of range

# The equivalent to JavaScript’s push() method is append():
colors.append('purple')
print(colors)
# prints: ['red', 'green', 'brown', 'purple']
# purple was added to the end of the list

# However, unlike JavaScript’s push() method, append() can only add one item and does not return a value.
# For adding multiple items, use the extend():
colors.extend(['orange', 'black'])
print(colors)
# prints: ['red', 'green', 'brown', 'purple', 'orange', 'black']
# orange and black were added to the end of the list

# To add an item anywhere within a list, use the insert() method:
colors.insert(1, 'yellow')
print(colors)
# prints: ['red', 'yellow', 'green', 'brown', 'purple', 'orange', 'black']
# yellow was added at the 1 index; no elements were replaced

# Python lists have a pop() method, but it’s more flexible in Python 
# because you can specify the index of the item to remove and return:
green = colors.pop(2)
print(colors)
# prints: ['red', 'yellow', 'brown', 'purple', 'orange', 'black']
# green was removed at the 2 index and is in the green variable

# There’s also a remove() method that removes the first item that matches what you pass in:
colors.remove('orange')
print(colors)
# prints: ['red', 'yellow', 'brown', 'purple', 'black']

# The clear() method empties a list:
colors.clear()
print(colors)
# prints: []

# The for in loop is used to iterate over the items in a list:
colors = ['red', 'green', 'blue']
for color in colors:
    print(color)
    # prints:
    # red
    # green
    # blue

# If we need to access the index of the item while iterating over a list, we use the built-in 
# enumerate() function to provide the index and the value to a for loop:
for idx, color in enumerate(colors):
    print(idx, color)
    # prints:
    # 0 red
    # 1 green
    # 2 blue

# If you need to create a 1-tuple (a tuple with one item), note that a comma is necessary:
hello_tuple = ('Hello')
# this will not create a tuple
print(type(hello_tuple))
# prints: <class 'str'>

hello_tuple = ('Hello',)
# or just the following (remember parenthesis are not required)
hello_tuple = 'Hello',
print(type(hello_tuple))
# prints: <class 'tuple'>

# Although tuples can’t be modified like lists, 
# we can retrieve their items in the same way using square brackets:
colors = ('red', 'green', 'blue')
print(colors[1])
# prints: green

# Sequences (lists, tuples, and strings) also have an index() 
# method that returns the index of the first match:

colors = ('red', 'green', 'blue')
blue_idx = colors.index('blue')
print(blue_idx)
# prints: 2

# The items in tuples are iterated over by using for loops, as we saw previously with lists:
for idx, color in enumerate(colors):
    print(idx, color)
    # prints:
    # 0 red
    # 1 green
    # 2 blue
    
# Tuples (and other sequences) have a convenient feature called unpacking. 
# This performs multiple variable assignments in a single line of code:
colors = ('red', 'green', 'blue')
r, g, b = colors
print(r, g, b)
# prints: red green blue

# It requires comma-separated variables on the left side of the assignment operator 
# and a sequence of values on the right. Functions and methods often return tuples in 
# Python, which is often the preferred method of accessing them.
# You’ve already seen this in action within the for in loops while 
# working with dictionaries. Recall this example:

for key, val in student.items():
    print( f"{key} is {val}" )

# Create a set from scratch using curly braces:
integer_set = {1, 2, 3, 4, 5}

# Or, more commonly, create a set from an iterable data type, like a list or tuple.
another_int_set = set([5, 6, 7, 8, 9])
chips = ['potato', 'computer', 'fish and']
chips_set = set(chips)

# In Python, you can add elements to a set using the add() method.
# Adding elements to a set
chips_set.add('paint')
print(chips_set)
# prints: {'paint', 'fish and', 'potato', 'computer'}
# remember, sets are not ordered - your elements may print in a different order

# To remove elements from a set in Python, you can use the remove() method.
# Removing elements from a set
chips_set.remove('fish and')
print(chips_set)
# prints: {'potato', 'paint', 'computer'}
# remember, sets are not ordered - your elements may print in a different order

# Say we needed to square all of the numbers in a list and put them into a new list, 
# we might use a for loop like this:
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = []
# we want 'n * n' for each 'n' in nums 
for n in nums:
    squares.append(n * n)
print(squares)
# prints [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# A list comprehension can reduce this code:
squares = []
for n in nums:
    squares.append(n * n)
    # To this:
    squares = [n * n for n in nums]
    
# Here’s the basic syntax of a list comprehension:
# [<expression> for <item> in <list>]
# This reads as: I want <expression> for each <item> in <list>

# We just saw how list comprehensions are an excellent way to map a 
# list, but they can be used for filtering too.
# Again, let’s start with a non-comprehension approach by using a for 
# in loop to map and filter nums:
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = []
# we want 'n * n' for each 'n' in nums  if 'n * n' is even
for n in nums:
    square = n * n 
    if square % 2 == 0:
        even_squares.append(square)
print(even_squares)
# prints: [4, 16, 36, 64, 100]

# Again, list comprehensions reduce the above from:
even_squares = []
for n in nums:
    square = n * n 
    if square % 2 == 0:
        even_squares.append(square)
# To this one-liner:
even_squares = [n * n for n in nums if (n * n) % 2 == 0]