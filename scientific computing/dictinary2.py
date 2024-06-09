# Dictionary keys must be immutable objects like strings, booleans, floats, integers, or tuples.
# Lists are not immutable, hence cannot be used as keys.
# Keys in a dictionary must be unique.

# Creating the dictionary
dictionary = {'spain': 'madrid', 'usa': 'vegas'}

# Print the initial dictionary
print("my initial dictionary:", dictionary)

# Adding a new entry with key 'france'
dictionary['france'] = 'paris'
print("Added 'france' entry:", dictionary)

# Removing the entry with key 'spain'
del dictionary['spain']
print("Removed 'spain' entry:", dictionary)

# Checking if 'france' is a key in the dictionary
print("'france' in dictionary:", 'france' in dictionary)

# Removing all entries in the dictionary
dictionary.clear()
print("Cleared dictionary:", dictionary)