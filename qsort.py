#!/usr/bin/python

import random

def lessthan(test, pivot):
    return test < pivot

def greaterthan(test, pivot):
    return pivot < test

def partition(a, left, right, predicate):

    pivot = a[right]

    il = left
    ir = right

    while il < ir:
        while il < right and predicate(a[il], pivot):
            il += 1
    
        while ir >= left and not predicate(a[ir], pivot):
            ir -= 1
    
        if il < ir:
            a[il], a[ir] = a[ir], a[il]

    a[il], a[right] = a[right], a[il]

    return il

def _qsort(a, left, right, predicate):

    if (right <= left):
        return

    i = partition(a, left, right, predicate)

    if left < i - 1:
        _qsort(a, left, i - 1, predicate)

    if i + 1 < right:
        _qsort(a, i + 1, right, predicate)

def qsort(a, predicate=lessthan):

    _qsort(a, 0, len(a) - 1, predicate)
    
def test_qsort():

    nfrom = 0
    nto = 15
    nelements = 19

    a = [random.randint(nfrom, nto) for x in range(nelements)]

    qsort(a, greaterthan)

    if not sorted(a, reverse=True) == a:
        print a

def main():

    for i in range(100):
        test_qsort()

if __name__ == '__main__':
    main()
