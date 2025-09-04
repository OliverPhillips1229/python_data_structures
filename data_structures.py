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