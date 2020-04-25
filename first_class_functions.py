# a first class function is an entity which supports all the operations generally available to other entities. These operations typically include being passed as an argumetn, returned from a function, and assigned to a variable.

# what does this mean? we can treat functions like any other object or vairable.


def square(x):
    return x * x


# f = square(5)
# print(f)

# ok so we are going to take away the parenthasis on line 10 with the 5 in it.

f = square
print(f(5))

# so we have assigned a function as a variable

# we can also pass functions as arguments
