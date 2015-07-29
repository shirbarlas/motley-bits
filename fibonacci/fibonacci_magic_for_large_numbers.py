#
# read: http://codeforces.com/blog/entry/14385
#
from time import time
from sys import argv

F = {0: 1, 1: 1}

def f(n):
    M = 10**40  # last X digits from fibonacci nth number

    if F.has_key(n):
        return F[n]

    K = n / 2

    if n % 2 == 0:
        F[n] = (f(K) * f(K) + f(K - 1) * f(K - 1)) % M
        return F[n]
    else:
        F[n] = (f(K) * f(K + 1) + f(K - 1) * f(K)) % M
        return F[n]


if __name__ == "__main__":
    start = time()
    print f(int(argv[1]))
    computation_time = time() - start
    print('\n\nCalculation time : ' + str(computation_time) + ' seconds')
