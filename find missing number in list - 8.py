def find_missing_number(list_in):
	for i in range(max(list_in)):
		if i not in list_in:
			print(i)
find_missing_number([6,10,2,5,4])
