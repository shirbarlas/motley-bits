"""
Fibonacci using recursion
"""

from sys import argv
from time import time

def fib(n):
    if n == 1 or n == 2:
        return 1

    return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    start = time()
    print fib(int(argv[1]))
    computation_time = time() - start
    print('\n\nCalculation time : ' + str(computation_time) + ' seconds')
