#!/usr/bin/python

"""
This is my version of the quicksort algorithm. This version
assumes that the input array has only distinct elements. Will update
this code at a future date to accomodate for repeated elements.
"""


import numpy as np

# in-place partitioning (partition as elements are revealed with repeated swaps)
# runs in linear time O(n)
def partition(A, l, r):
    # pivot WLOG is considered to be the first element
    p = A[l]
    i = l + 1
    for j in range(l+1,r+1):
        if A[j] < p: # otherwise do nothing and increase pointer j
            # swap A[i] with A[j]
            A[i], A[j] = A[j], A[i]
            i += 1
    # finally swap A[i-1] with A[l] to place pivot in correct position
    A[i-1], A[l] = A[l], A[i-1]
    return i-1

def choosePivot(A,l=None,r=None):
    """
    This function will choose a pivot for the considered
    subset of A = [a_l,...,a_r]. It also does the 
    swap to put the pivot in the ell-th position. This is 
    required because the parition function assumes that
    the pivot element is located in the first element of
    the subset A.
    """
    if l == None:
        l = 0
    if r == None:
        r = len(A) - 1
    p = np.random.randint(l,r+1, size = 1)[0]
    # pre-process A now, so that the pivot is the first element of array 
    A[l],A[p] = A[p],A[l]
    return p

# QuickSort algorithm done completely in place using repeated swaps implemented through recursions
def quickSort(A,l=None,r=None):
    """
    input: A = [a_l,...,a_r]
    l and r are specified in the algorithm in recursive steps
    so that the repeated swaps are done in place
    """
    if r == None:
        r = len(A)-1 # index of last element in A
    if l == None:
        l = 0 # index of first element in A
    
    n = r-l+1
    if n <= 1: # less than one to handle the case if L and R are empty after the random partition
        return A
    else:
        choosePivot(A,l,r)
        ix = partition(A,l,r)
        quickSort(A, l, ix-1)
        quickSort(A, ix+1,r)
