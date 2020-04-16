def capital_letter_reversed(string1):
  string1_list = list(string1)
  vowels = ""
  char_id = []
  i = 0
  for char in string1:
    if char in "aeiouAEIOU":
        vowels = vowels + char
        char_id.append(i)
    i += 1
  vowels = vowels[::-1]
  vowels_list = list(vowels)
  for index, item in enumerate(char_id):
      string1_list[item] = vowels_list[index]

  return(''.join(string1_list))

print(capital_letter_reversed("aec"))