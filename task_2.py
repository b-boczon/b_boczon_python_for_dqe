import random
import string

# Use dict comprehension inside list comprehension to create list of dictionaries, range of items inside dict is limited to 10 for readability 
list_of_dicts = [{random.choice(string.ascii_letters): random.randint(0,100) for j in range(random.randint(1, 10))} for i in range(random.randint(2, 10))]

print(list_of_dicts)

# Initiate counter to store the count of each key and val to store the maximum value of each key
counter = {}
val = {}

# Enumerate over the list of dictionaries
for i, d in enumerate(list_of_dicts, 1):
    # Iterate over each key-value in the current dictionary
    for k, v in d.items():
        counter[k] = counter.get(k, 0) + 1  # Increment the count of the key in 'counter'
        if k not in val or v > val[k]:  # Update the value if the value is greater
            val[k] = v

# Create a new dictionary 'final_result' where each key is appended with its count from 'counter'
result = {f"{k}_{counter[k]}" if counter[k] > 1 else k: v for k, v in val.items()}

print(result)