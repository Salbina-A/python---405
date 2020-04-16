def factorial_recursive(n):
	number = 1
	while n >= 1:
		number = number*n
		n = n -1
	return number
print (factorial_recursive(5))