#!/bin/python
"""
This python script counts the number of inversions in a given array. It piggy backs off of the merge sort algorithm contained in merge_sort.py.

Inversion algorithm represents another application of the divide and conquer paradigm.
"""

def merge_and_count_split(B,C):
	"""
	This function combines the two subarrays in the sort_and_count procedure
	and also counts the number of split inversions.
	"""
	D = []
	# this assumes that x and y are lists of the same magnitude
	n = len(B)
	nsplits = 0 # counter for split inversions
	# starting positions for our pointers
	i = 0
	j = 0
	while i < n and j < n:
		if B[i] < C[j]:
			D.append(B[i])
			i += 1
		else:
			D.append(C[j])
			nsplits += n-i # number of elements remaining in the B array
			j += 1
	# append the remaining symbols
	# split inversions have all been counted
	if j < i: 
		for el in C[j:]:
			D.append(el)
	else:
		for el in B[i:]:
			D.append(el)
	return [D, nsplits]


def sort_and_count(A):
	"""
	This recursive function returns the number of inversions in an array as 
	well as the sorted array
	"""
	n = len(A)
	if n == 1:
		return [A,0]
	else:
		half = int(n/2)
		# sort and count left inversions of the left half of array A
		B, x = sort_and_count(A[:half])
		# sort and count right inversions of the right half of array A
		C, y = sort_and_count(A[half:])
		# merge and count split inversions
		D, z = merge_and_count_split(B,C)
	return [D,x+y+z]
