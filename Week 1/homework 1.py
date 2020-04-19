def all_positive(*args):
	return any (x<0 for x in args)
print(all_positive(1))