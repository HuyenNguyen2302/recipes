# define 'constant' N
N = 10

# define 'constant' size - number of elements
SIZE = 5

def countingSort(A):
	"This function implements counting sort"
	list = [0] * N
	for i in xrange(SIZE):
		index = A[i]
		list[index] += 1
	
	print list

	for i in xrange(1, SIZE):
		list[i] = list[i-1] + list[i]

	print list

	B = [0] * SIZE

	for i in xrange(SIZE - 1, -1, -1):
		indexList = A[i]
		list[indexList] -= 1
		indexB = list[indexList] 
		B[indexB] = indexList

	print B
	

# Test case
A = [3, 4, 2, 3, 1]
countingSort(A)
