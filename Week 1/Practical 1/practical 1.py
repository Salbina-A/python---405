def implication3(a, b, c):

	d = bool( not (b) or c)
	f = bool(not(a) or d)
	return f

print(implication3(1, 0, 0))



def last_digit(N):
	summ = 0
	for i in range(1, N+1):
		summ = summ + (i*i)
		ld = summ%10
	return ld
print(last_digit(950))
