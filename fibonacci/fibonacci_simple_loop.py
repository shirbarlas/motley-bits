"""
Fibonacci using loop
"""

from sys import argv

def fib(n):
    a, b = 1, 1

    for i in range(n-1):
        a, b = b, a+b

    return a

if __name__ == "__main__":
    print fib(int(argv[1]))
