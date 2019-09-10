"""
Define the generator function fib_gen, which is capable of yielding 
values of infinite fibonacci series.

For e.g : You should able to create a generator fs from fib_gen and if 
fs is accessed using next for four times, then it should yield 
values 0, 1, 1, 2. You may type python3.5 to use the latest version for the exercise
"""


def fib_gen():
    """ Generator yielding Fibonacci numbers
    
    :returns: int -- Fibonacci number as an integer
    """
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y