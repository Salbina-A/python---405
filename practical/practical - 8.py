def maximum_list(a):
	i = (a.index(max(a)))
	b = a.pop(i)
	for j in range(len(a)):
		if a[j] != a[j-1]:
			print(max(a))
		else:
			print(0.5)
		break
maximum_list([1, 5, 6, 4, 2])