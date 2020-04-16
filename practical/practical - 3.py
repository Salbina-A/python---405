int_list = [101, 110, 220, 100, 103, 606, 603]
count = 0
out_list = []
for item in range(len(int_list)):	
	a = [int(i) for i in str(int_list[count])]
	count+=1	
	for j in range(len(a)):
		if a[j] == a[j-1]:
			print((int_list[item]))
			
