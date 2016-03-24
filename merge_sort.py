#!/bin/python

# My merge sort algorithm

def combine(x,y):
	z = []
	# this assumes that x and y are lists of the same magnitude
	n = len(x)
	# starting positions for our pointers
	i = 0
	j = 0
	while i < n and j < n:
		if x[i] < y[j]:
			z.append(x[i])
			i += 1
		else:
			z.append(y[j])
			j += 1
	# append the remaining symbols
	if j < i:
		for el in y[j:]:
			z.append(el)
	else:
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