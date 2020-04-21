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
inp_list = ["Name1","" , "", "", "Name2", ""]

only_names = lambda i: [i for i in inp_list if i != ""]
print(only_names(inp_list))

	
print(only_names(["Name0", "", "Name1", "", "Name2", "" ]))

#7th task
discriminant  = lambda a, b, c: ((b*b - 4*a*c))
print(discriminant (1, 2, 1))

#8th task

list1 = ["Name0", "Name1"]
list2 = ["L_Name0", "L_Name1"]

full_name = (lambda i: [" ".join(map(str, i)) for i in zip(list1, list2)])

print(full_name(0))

