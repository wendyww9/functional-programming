# Wave 1
# Write a function that takes in a list of words and returns the shortest
# one. (assume no ties)

# def shortest_word(words):
#     return min(words, key=len)

# SUPER CHALLENGE: use functools.reduce
# Only try this after completing the rest of the activity
# You will need to research the use of the functools.reduce function
def shortest_word(words):
    from functools import reduce
    return reduce(lambda x , y: x if len(x) < len(y) else y, words)   


# Wave 2
# Write a function that takes in a list of numbers and returns a new list
# containing only the ones that are even, in the same order.
# Hint: remember to convert back to a list!

def even_nums(nums):
    return list(filter(lambda x: x % 2 == 0, nums))

# Wave 3
# Write a function that takes in a list of numbers and returns a new list
# containing the squares of those numbers (the numbers raised to the second power)
# Hint: remember to convert back to a list!

def squares(nums):
    return list(map(lambda x: x * x, nums))

# Wave 4
# Write a function that accepts a word, a function, and the name of that 
# function. It should return a string that reports:
# "The result of applying FUNCTION_NAME to WORD is RESULT"

def report(word, function, function_name):
    return f"The result of applying {function_name} to {word} is {function(word)}"

# Wave 5
# Write a function that takes a list of passwords and returns a list of only 
# those passwords that have at least one non-alphabetic character in them. 
# The returned list should be sorted by in order of increasing length.

def sorted_valid_passwords(passwords):
    return list(sorted(filter(lambda s: not s.isalpha(), passwords ), key=len))

