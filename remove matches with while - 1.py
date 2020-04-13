def remove_from_list(inp_list, remove_item):
	while remove_item in inp_list:
		inp_list.remove(remove_item)
	print(inp_list)
		

remove_from_list([[1, 2], [1, 2, 3], [1, 2]], [1, 2])
