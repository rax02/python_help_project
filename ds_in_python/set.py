# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding an element to the set
my_set.add(6)
print("After adding 6:", my_set)

# Removing an element from the set
my_set.remove(3)
print("After removing 3:", my_set)

# Checking if an element is in the set
print("Is 4 in the set?", 4 in my_set)

# Union of two sets
another_set = {4, 5, 6, 7, 8}
union_set = my_set.union(another_set)
print("Union of sets:", union_set)

# Intersection of two sets
intersection_set = my_set.intersection(another_set)
print("Intersection of sets:", intersection_set)

# Difference of two sets
difference_set = my_set.difference(another_set)
print("Difference of sets:", difference_set)

# Clearing the set
my_set.clear()
print("After clearing the set:", my_set)