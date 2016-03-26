#!/usr/bin/python

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
    return A[:i-1],[A[i-1]],A[i:]

def choosePivot(A):
    p = np.random.randint(0,len(A), size = 1)[0]
    # pre-process A now, so that the pivot is the first element of array 
    A[0],A[p] = A[p],A[0]

def quickSort(A):
    n = len(A)
    if n < 1: # less than one to handle the case if L and R are empty after the random partition
        return A
    else:
        choosePivot(A)
        L, p, R = partition(A, 0, n-1) # index of pivot
        return quickSort(L) + p + quickSort(R) 