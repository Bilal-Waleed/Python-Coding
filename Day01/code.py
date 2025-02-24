# What is the anwer to this question?

from functools import partial
def add(x, y, z):
    return x + y + z
add_five = partial(add, 5)
print(add_five(3, 2))

# Answer: 10 