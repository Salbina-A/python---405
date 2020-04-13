def symm_str(inp_str):
	for i in range(len(inp_str)):
		if inp_str == inp_str[::-1]:
			return True
		else:
			return False
print(symm_str("121"))


