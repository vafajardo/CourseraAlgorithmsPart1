#!/usr/bin/python

"""
This python script is an implementation of the Random Selection algorithm (RSelect).

Statement of Problem:
- Input array A with n distinct (for simplicity) numbers and a number i in {1,2,...,n}.
- Output the i-th order statistic of the array A.

Functions/Sub Procedures used:
- partition()
- choosePivot() 
*both of which were used in QuickSort algorithm.

Val Andrei Fajardo
"""

import numpy as np

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
    return i-1 # returns index of the pivot

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

def RSelect(A,i, l=None, r=None):
    """
    Input array=A, orderstat=i, A=[a_l,...,a_r] where l,r take values in (0,1,...,len(A)-1)
    Swaps are done in place via paritition and choosePivot functions
    """
    if r == None:
        r = len(A)-1 # index of last element in A
    if l == None:
        l = 0 # index of first element in A
    
    n = r-l+1
    if n == 1:
        return A[l] 
        """
        because we are swapping in place, 
        the median will end up in ell-th position 
        when recursions reduce down to base case
        """
    else:
        p = choosePivot(A,l,r)
        ix = partition(A,l,r) # gives the index of the pivot after partition
        # A[l:r] = [a_l,...a_ix,...a_r] 
        j = ix - l + 1 # the pivot is actually the j-th order statistic of the subarray A[l:r] where j=ix-l+1 
        #print 'i:',i,'j:',j, 'ix:',ix, A[l:r+1]
        if j == i:
            return A[ix]
        elif j > i:
            return RSelect(A,i,l,ix-1)
        else:
            return RSelect(A,i-j,ix+1,r)  
