#!/bin/python

# My merge sort algorithm (can handle non-even arrays)

def combine(x,y):
	"""
	merge_sort always sends y as bigger half in case x and y
	are arrays of different lengths.
	I have to include "=" to take this last observation into account.
	"""
	z = []
	# having nx and ny allows for combinin
	nx = len(x)
	ny = len(y) 
	# starting positions for our pointers
	i = 0
	j = 0
	while i < nx and j < ny:
		if x[i] < y[j]:
			z.append(x[i])
			i += 1
		else:
			z.append(y[j])
			j += 1
	# append the remaining symbols
	if j <= i: # include "=" here since y is bigger half in case of uneveness
		for el in y[j:]:
			z.append(el)
	else: # there are elements in remaining in x
		for el in x[i:]:
			z.append(el)
	return z

def merge_sort(x):
	n = len(x)
	half = int(n/2)
	if n == 1:
		return [x[0]] # returns a list in basic case
	else:
		foo = merge_sort(x[:half])
		bar = merge_sort(x[half:])
		return combine(foo,bar)
		
		