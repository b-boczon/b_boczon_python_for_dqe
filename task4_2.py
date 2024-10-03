import random
import string

# Generate a list of dictionaries using list comprehension and dict comprehension
list_of_dicts = [{random.choice(string.ascii_letters.upper()): random.randint(0, 100) for _ in range(random.randint(1, 10))} for _ in range(random.randint(2, 10))]

# Function to merge dictionaries by finding the highest value for each key and its respective index

def merge_dicts(dicts):
    """This function enumerates through the list of dictionaries with index starting from 1. Next, through each
    key-value pair in the dictionary, then if the key is not in key_sources or the current value is higher than
    the stored value, update key_sources with the new higher value and the index of that dictionary"""
    key_sources = {}
    for i, d in enumerate(dicts, 1):
        for key, value in d.items():
            if key not in key_sources or value > key_sources[key][0]:
                key_sources[key] = (value, i)
    return key_sources

def build_final_result(dictionaries, key_sources):
    """This function iterates through key_sources to construct the final result dictionary, check if the key appears in
    more than one dictionary, if yes, append the index of the dictionary with the highest value to the key,
    if no, ads normally
    """
    result = {}

    for key, (value, i) in key_sources.items():
        # check if the key appears in more than one dictionary
        if sum(key in d for d in dictionaries) > 1:
            # if yes, append the index of the dictionary with the highest value to the key
            result[f"{key}_{i}"] = value
        else:
            # if the key is only in one dictionary, add normally
            result[key] = value
    return result


print(list_of_dicts)
print(build_final_result(list_of_dicts, merge_dicts(list_of_dicts)))
