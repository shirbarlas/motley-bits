"""
Fibonacci using loop
"""

from sys import argv
from time import time

def fib(n):
    a, b = 1, 1

    for i in range(n-1):
        a, b = b, a+b

    return a

if __name__ == "__main__":
    start = time()
    print fib(int(argv[1]))
    computation_time = time() - start
    print('\n\nCalculation time : ' + str(computation_time) + ' seconds')
