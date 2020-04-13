def sum_in_bin(num_inp):
	bin_num = "{0:b}".format(num_inp)
	print ( sum(int((bin_num))))
sum_in_bin()