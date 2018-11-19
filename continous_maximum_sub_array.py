def maxsubArraySum(a,size):

	max_so_far = a[0]
	curr_max =   a[0]


	for i in range(1,size):
		curr_max = max(a[i],curr_max+a[i])
		max_so_far = max(max_so_far,curr_max)

	return max_so_far
	

A = a = [-2, -3, 4, -1, -2, 1, 5, -3]
print("Maximum contigous sum is : ", maxsubArraySum(a,len(a)))		