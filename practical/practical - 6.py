string1 = "abc"
string2 = "befca"
string3 = ""
for i in range(len(string2)):
	if string2[i] in string1:
		count_el = string1.count(string2[i])
		string3 = string3 + count_el*string2[i]
print(string3)

		

