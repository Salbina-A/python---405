def implication3(a, b, c):
	return bool(a or (b and c))

print(implication3(0, 0, 0))