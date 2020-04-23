#1st taks
def implication3(a, b, c):

	d = ( not (b) or c)
	f = (not(a) or d)
	return f

print(implication3(1, 0, 0))

#2nd task
def expr_vale(inp_str):
	for i in inp_str:
		return (eval(inp_str))
print(expr_vale("1*2+9"))

#3rd task
def quick_or(bool_list):
	return (any(bool_list))
print(quick_or(([False, False, False, False, False, False])))

#5th task
def last_digit(N):
	summ = 0
	for i in range(1, N+1):
		summ = summ + (i*i)
		ld = summ%10
	return ld
print(last_digit(1254))
