#1st task
def bisect_position(int_list, add_num):
	if add_num > max(int_list):
			return(len(int_list))
	else:


		int_list.append(add_num)
		for i in int_list:
			for i in range(len(int_list)-1):
				
				if int_list[i] > int_list[i+1]:	
									
					int_list[i] = int_list[i] + int_list[i+1]
					int_list[i+1] = int_list[i] - int_list[i+1]
					int_list[i] = int_list[i] - int_list[i+1]
					
					return(i)
			

print(bisect_position([1, 2, 5, 1, 7], 8))
#P.S. works partly



#2nd task
def all_sums(inp_num):	
	first_ind = 0
	last_ind = 0

	a = [item for item in range(1, inp_num)]
	for i in range(int(len(a)/2)):
		b = (a[first_ind], a[last_ind - 1])
		print(b, end = " ")
		first_ind += 1
		last_ind -= 1
		
	
(all_sums(7))


#3rd task
from collections import defaultdict

def duplicate_characters(inp_str):
	d = defaultdict(int)
	for k in inp_str.replace(" ", ""):
		d[k] += 1
	set_ret = set()
	for char in sorted(d, key = d.get):
		if d[char] > 1:
			set_ret.add(char)
	return(set_ret)

print(duplicate_characters('Here we have some duplicates'))




#4th task
def compare_lists(int_list1, int_list2):
	if len(int_list1) != len(int_list2):
		return False
	else:

		for i in int_list1:
			for i in range(len(int_list1)-1):
				if int_list1[i] > int_list1[i+1]:
						int_list1[i] = int_list1[i] + int_list1[i+1]
						int_list1[i+1] = int_list1[i] - int_list1[i+1]
						int_list1[i] = int_list1[i] - int_list1[i+1]

		for i in int_list2:
			for i in range(len(int_list2)-1):		
				if int_list2[i] > int_list2[i+1]:
						int_list2[i] = int_list2[i] + int_list2[i+1]
						int_list2[i+1] = int_list2[i] - int_list2[i+1]
						int_list2[i] = int_list2[i] - int_list2[i+1]

		if int_list1 == int_list2:
			return True
		else:
			return False

print(compare_lists([6,1,1,4], [4,1,1,6]))


#5th task


#6th task
def sort_list(int_list, order):

	for i in int_list:
		for i in range(len(int_list)-1):
			if int_list[i] < int_list[i+1] and order == "descending":
				int_list[i] = int_list[i] + int_list[i+1]
				int_list[i+1] = int_list[i] - int_list[i+1]
				int_list[i] = int_list[i] - int_list[i+1]

			if int_list[i] > int_list[i+1] or  order == "ascending":
				int_list[i] = int_list[i] + int_list[i+1]
				int_list[i+1] = int_list[i] - int_list[i+1]
				int_list[i] = int_list[i] - int_list[i+1]
	print(int_list)


	

sort_list([1, 5, 7, 9, 1, 3, 0, -1], "descending")

