def hasArrayTwoCandidates(A,arr_size,sum):

	# sort the array
	quickSort(A,0,arr_size-1)
	l=0
	r = arr_size-1

	while l<r:
		if (A[l]+A[r]==sum):
			return 1
		elif (A[l]+A[r]<sum):
			l+=1
		else:
			r -= 1
	return 0
	

def quickSort(A,si,ei):
	if si<ei:
		pi = partion(A,si,ei)
		quickSort(A,si,pi-1)
		quickSort(A,pi+1,ei)

			
			
