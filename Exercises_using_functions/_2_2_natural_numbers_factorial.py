"""
Define the generator function factorial_gen, which is capable of 
yielding factorial values of natural numbers.

For e.g : You should able to create a generator fs from 
factorial_gen and if fs is accessed using next for five times, 
then it should yield values 1, 1, 2, 6,24, 120,...
"""


def factorial_gen():
    """ Generator yielding Factorial values of natural numbers
    
    :returns: int -- Factorial value
    """
    x, y = 1, 2
    while True:
        yield x
        x, y = x * y, y + 1