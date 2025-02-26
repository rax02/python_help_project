# Creating a dictionary
my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

# Accessing values
print(my_dict['name'])  # Output: Alice

# Adding a new key-value pair
my_dict['email'] = 'alice@example.com'
print(my_dict)

# Updating an existing key-value pair
my_dict['age'] = 26
print(my_dict)

# Removing a key-value pair using pop()
removed_value = my_dict.pop('city')
print(f'Removed value: {removed_value}')
print(my_dict)

# Removing the last inserted key-value pair using popitem()
last_item = my_dict.popitem()
print(f'Last item: {last_item}')
print(my_dict)

# Getting a value using get()
age = my_dict.get('age')
print(f'Age: {age}')

# Getting all keys using keys()
keys = my_dict.keys()
print(f'Keys: {keys}')

# Getting all values using values()
values = my_dict.values()
print(f'Values: {values}')

# Getting all key-value pairs using items()
items = my_dict.items()
print(f'Items: {items}')

# Checking if a key exists in the dictionary
if 'name' in my_dict:
    print('Name is a key in the dictionary')

# Clearing all items in the dictionary
my_dict.clear()
print(f'Dictionary after clearing: {my_dict}')