# importing randint for producing a random number
from random import randint 

# using list comprehension create list of 100 values in range from 0 to 1000 
lst = [randint(0,1000) for i in range(100)] 

# sorting list using nested loops by comapring every value with every value in the list one by one 
# and if the first number is bigger than second it swaps their places
for i in range(0, len(lst)):
    for j in range(i+1, len(lst)):        
        if lst[i] >= lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

# using list comprehensions with conditional logic to divide into even and odd numbers list
# if the remainder from the division by 2 is equal to 0 then it is a even number
evens = [i for i in lst if i%2==0]
# if the remainder from the division by 2 is equal to 1 then it is a odd number
odds = [i for i in lst if i%2==1]

# printing out a average - summing the values in the list and dividing it by number of values
print(sum(evens)/len(evens)) 
print(sum(odds)/len(odds))

