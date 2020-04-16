string1 = "america"
vowels = ""
ind = 0
final_str = ""
for char_id in string1:
	if char_id in "aeiouAEIOU":
		vowels = vowels + char_id
		if ind < len(string1):
			print(vowels[ind])
			ind += 1


print(vowels[::-1])

