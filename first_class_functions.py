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

# we can also pass functions as arguments and return functions as a result of other functions --> these are higher order functions.


def cube(x):
    return x * x * x


def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result


squares = my_map(cube, [1, 2, 3, 4, 5])

print(squares)


# so a lot happening above. we are creating the my_map function, which takes a function. we are creating the result empty array, looping through the arg_list, appending to our empy array each item from the arg_list after it has passed through the function that is an argument.

# i added the cube function to this, and now the results are cubed. so it's helpful to see here why a higher order function would be useful.
