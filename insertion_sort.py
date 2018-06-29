#!/usr/bin/python

import random

def lessthan(test, pivot):
    return test < pivot

def greaterthan(test, pivot):
    return pivot < test

def isort(a):
    # insertion sort grabs the next element from the unsorted part of the 
    pass
    
def test_isort():

    nfrom = 0
    nto = 15
    nelements = 19

    a = [random.randint(nfrom, nto) for x in range(nelements)]

    isort(a, greaterthan)

    if not sorted(a, reverse=True) == a:
        print a

def main():

    for i in range(100):
        test_isort()

if __name__ == '__main__':
    main()
