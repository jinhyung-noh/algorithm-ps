def recursion(i):
	if i>10:
		return

	print(i)
	recursion(i+1)
	print(i)
recursion(0)
