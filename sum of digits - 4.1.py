def sum_of_digits(n):
	s = 0
	n = abs(n)
	i = 0
	while n >= 10**i:
		i += 1
	for j in range(i):
		s = s + n%10
		n = n//10
	return s
print(sum_of_digits(4556))