#!/usr/bin/python

import random
from pprint import pprint, pformat


def isort(a):
    # insertion sort grabs the next element from the unsorted part of the array
    l = len(a)

    for i in xrange(l - 1):
        j = i + 1
        m = a[j]
        while j > 0 and a[j - 1] >= m:
            a[j] = a[j - 1]
            j -= 1
        a[j] = m


def test_isort():
    nfrom = 0
    nto = 1511
    nelements = 1000

    a = [random.randint(nfrom, nto) for x in range(nelements)]

    isort(a)

    if not sorted(a) == a:
        print a


def main():
    for i in range(100):
        test_isort()


if __name__ == '__main__':
    main()
