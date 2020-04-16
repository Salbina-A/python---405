def is_same(list_1, list_2):
	state = "False"
	for x in list_1:
  		if list_1 == list_2:
  			state = "True"
  			break
  		list_1 = list_1[1:] + list_1[:1] 
	return state
print(is_same([1, 2, 3], [2, 3, 5]))