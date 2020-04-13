def greatest_comm_div(a,b):
	if b == 0:
		return a
	else:
		return (greatest_comm_div(b, a%b))
print (greatest_comm_div(7,5))