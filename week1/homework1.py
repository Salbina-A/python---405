# 1st task
def all_positive(*args):
	return any (x<0 for x in args)
print(all_positive(1))


#2nd task
def xor3(a, b, c):
	i = bool((a and not b) or (not a and b))
	j = bool((i and not c) or (not i and c))
	return(j)
print(xor3(0, 0, 0))

#3rd task
def binary_sum(inp_str):
	new_string = ""
	for char in inp_str:
		n = ord(char)
		if 96 <= n <= 122:
			n = n+(110-n)*2-1
			
		
		if 65 <= n <= 90:
			n = n = n+(78-n)*2-1
		char = chr(n)
		new_string += char
	

	return (new_string)
print(binary_sum('Hello World!'))

#4th task


#5th task
def binary_sum(str1, str2):
	return (int(str1, 2) + int(str2, 2))

print(binary_sum("1", "10" ))


#6th task
def only_names(inp):
	check_names = filter(lambda x: x!= "", inp)
	filtered_names = list(check_names)
	return filtered_names
print(only_names(["Name0", "", "Name1", "", "Name2", "" ]))

#7th task
def discriminant(a, b, c):
	cal = lambda d: ((b*b - 4*a*c))
	return cal

disc = discriminant(4, 8, 0)
print(disc(1))


#8th task
def full_name(list1, list2):
	return list(map(lambda i: " ".join(i), zip(list1, list2)))
print(full_name(["Nairi", "Vlad"], ["Hakobyan", "Poghosyan"]))
