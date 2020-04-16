def implication3(a, b, c):
	return bool(a or (b and c))

print(implication3(0, 0, 0))



def last_digit(N):
	summ = 0
	for i in range(1, N+1):
		summ = summ + (i*i)
		ld = summ%10
	return ld
print(last_digit(950))
