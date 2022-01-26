"""
The List Comprehension feature also allows you to use conditions to populate the list.
Consider the objective of initializing a list with the even numbers from a list of
any whole numbers, for example the numbers 1,3,4,5,7,8,9. To find out if a number is
par, we use the condition number % 2 == 0, which checks whether the remainder of a division by 2 is zero.
The code below uses a loop to initialize the list of pairs.

integers = [1,3,4,5,7,8,9]
pairs = []
is number in integers:
    if number % 2 == 0:
        pairs.append(number)

Research how we can use List Comprehension to do the same as the code above.
"""

integers = [1, 3, 4, 5, 7, 8, 9]

# The "if" structure it's put after the "for" loop, filtering and putting the result of condition in the list
pairs = [number for number in integers if number % 2 == 0]

print(pairs)
