# Creating a tuple
my_tuple = (1, 2, 3, 4, 5, 2)

# count() method: Returns the number of times a specified value occurs in a tuple
count_of_twos = my_tuple.count(2)
print(f"Count of 2 in tuple: {count_of_twos}")

# index() method: Searches the tuple for a specified value and returns the position of where it was found
index_of_four = my_tuple.index(4)
print(f"Index of 4 in tuple: {index_of_four}")

# Accessing elements in a tuple
first_element = my_tuple[0]
print(f"First element: {first_element}")

# Slicing a tuple
sub_tuple = my_tuple[1:4]
print(f"Sliced tuple: {sub_tuple}")

# Checking if an element exists in a tuple
is_three_in_tuple = 3 in my_tuple
print(f"Is 3 in tuple: {is_three_in_tuple}")

# Length of a tuple
tuple_length = len(my_tuple)
print(f"Length of tuple: {tuple_length}")