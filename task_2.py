import random
import string

# use dict comprehension inside list comprehension to create list of dictionaries, range of items inside dict is limited to 10 for readability 
list_of_dicts = [{random.choice(string.ascii_letters.upper()): random.randint(0,100) for j in range(random.randint(1, 10))} for i in range(random.randint(2, 10))]

# dictionary to store the final result
result = {}
# dictionary to track the highest value for each key and the index of the dictionary with that value
key_sources = {}

# enumerate through the list of dictionaries with index starting from 1
for i, d in enumerate(list_of_dicts, 1):
    # iterate through each key-value pair in the dictionary
    for key, value in d.items():
        # if the key is not in key_sources or the current value is higher than the stored value
        if key not in key_sources or value > key_sources[key][0]:
            # update key_sources with the new higher value and the index of that dictionary
            key_sources[key] = (value, i)

# iterate through key_sources to construct the final result dictionary
for key, (value, i) in key_sources.items():
    # check if the key appears in more than one dictionary
    if sum(key in d for d in list_of_dicts) > 1:
        # if yes, append the index of the dictionary with the highest value to the key
        result[f"{key}_{i}"] = value
    else:
        # if the key is only in one dictionary, add normaly
        result[key] = value


print(list_of_dicts)
print(result)
