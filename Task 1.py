# Creating a list
my_list = [1, 2, 3]
print("Initial list:", my_list)

# Adding an element
my_list.append(4)
print("List after adding an element:", my_list)

# Removing an element
my_list.remove(2)
print("List after removing an element:", my_list)

# Modifying an element
my_list[1] = 5
print("List after modifying an element:", my_list)


# Creating a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("\nInitial dictionary:", my_dict)

# Adding an element
my_dict['d'] = 4
print("Dictionary after adding an element:", my_dict)

# Removing an element
del my_dict['b']
print("Dictionary after removing an element:", my_dict)

# Modifying an element
my_dict['c'] = 5
print("Dictionary after modifying an element:", my_dict)


# Creating a set
my_set = {1, 2, 3}
print("\nInitial set:", my_set)

# Adding an element to the set
my_set.add(4)
print("Set after adding an element:", my_set)

# Removing an element from the set
my_set.remove(2)
print("Set after removing an element:", my_set)

my_set.remove(3)
my_set.add(5)
print("Set after modifying an element:", my_set)
