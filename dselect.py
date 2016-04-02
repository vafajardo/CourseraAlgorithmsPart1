#!/usr/bin/python

"""
This python script is of the Deterministic Selection algorithm.

Input: Array A (assumed to have distinct elements), integer i between 1 and 
the length of A
Output: The i-th order statistic of A

* Algorithms required: partition, and merge_sort (and thus combine)
** merge_sort is needed to find the median of medians
"""

def partition(A, l=None, r=None):
	"""
	input array is A[a_l,...,a_r] where a_l is the pivot
	"""
	if l == None:
		l = 0
	if r == None:
		r = len(A)-1
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

def combine(x,y):
	z = []
	# having nx and ny allows for combinin
	nx = len(x)
	ny = len(y) # my merge_sort function will always send y as the "bigger half" in case of uneveness
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
	if j <= i: # there are elements remaining in y (include = because j can equal to nx but still has one element left)
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

def firstrdmedians(A):
	n = len(A) 
	m = int(n/5)
	rem = n % 5
	C = []
	for i in range(m):
		C.append(merge_sort(A[i*5:(i+1)*5])[2])
	if rem != 0:
		if rem % 2 == 0 :
			mid = int(rem/2)
		else:
			mid = int((rem + 1)/2)
		C.append(merge_sort(A[-rem:])[mid-1])
	return C

def DSelect(A,i):
	assert i>= 1 and i <= len(A)
	n = len(A)
	if n <= 1: # base cases are any arrays with elements less than 5
		return A[0]
	else:        
		C = firstrdmedians(A)
		mid = int(len(C)/2)
		if len(C) == 1:
			p = C[0]
		else:
			p = DSelect(C, mid)
		# swap pivot postion into first position of A before calling on partition procedure
		foo = A.index(p)
		A[0],A[foo] = A[foo],A[0]
		#print 'A:',A, 'p:',p
		ix = partition(A)
		#print 'A after partition:', A
		# the pivot is the j-th order statistic of A where j=ix+1 (ix is index of pivot)
		j = ix + 1
		#print 'index of p:',ix, 'pivot is jth:',j
		if j == i:
			return p
		elif j > i:
			firstPartA = A[:ix]
			return DSelect(firstPartA,i)
		else:
			secondPartA = A[ix+1:]
			return DSelect(secondPartA,i-j) 