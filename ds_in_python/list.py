import copy

# Creating a list
my_list = [1, 2, 3, 4, 5]

# append() - Adds an element at the end of the list
my_list.append(6)
print("After append:", my_list)

# extend() - Adds all elements of a list (or any iterable) to the end of the current list
my_list.extend([7, 8, 9])
print("After extend:", my_list)

# insert() - Inserts an element at the specified position
my_list.insert(0, 0)
print("After insert:", my_list)

# remove() - Removes the first item with the specified value
my_list.remove(0)
print("After remove:", my_list)

# pop() - Removes the element at the specified position
my_list.pop(0)
print("After pop:", my_list)

# clear() - Removes all the elements from the list
my_list.clear()
print("After clear:", my_list)

# Creating a new list for further examples
my_list = [1, 2, 3, 4, 5, 3]

# index() - Returns the index of the first element with the specified value
index = my_list.index(3)
print("Index of 3:", index)

# count() - Returns the number of elements with the specified value
count = my_list.count(3)
print("Count of 3:", count)

# sort() - Sorts the list
my_list.sort()
print("After sort:", my_list)

# reverse() - Reverses the order of the list
my_list.reverse()
print("After reverse:", my_list)

# ---------------- copying the list

# copy() - Returns a shallow copy of the list
# Use case: When you need a new list with the same elements, but changes to the new list should not affect the original list.
copy_list = my_list.copy()
print("Copy of the list:", copy_list)

# Using slicing to copy the list
# Use case: Similar to copy(), creates a shallow copy. Useful for quick and concise copying.
sliced_copy = my_list[:]
print("Copy using slicing:", sliced_copy)

# Using list() constructor to copy the list
# Use case: Another way to create a shallow copy. Useful when you want to be explicit about creating a new list.
constructor_copy = list(my_list)
print("Copy using list() constructor:", constructor_copy)

# Using copy module's deepcopy to copy the list
# Use case: Creates a deep copy of the list. Useful when the list contains nested objects and you want to ensure all nested objects are also copied.
deep_copy = copy.deepcopy(my_list)
print("Copy using deepcopy:", deep_copy)



