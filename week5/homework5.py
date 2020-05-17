#1st task

class Roman_num(object):

	def int_converter_Rom(self, num):
		int_num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
		rom_num = ["M", "CM", "D", "CD", "C", "XC", "L", "XL","X", "IX", "V", "IV","I"]

		roman_num = ""
		i = 0
		while num > 0:
			for j in range(num // int_num[i]):
				roman_num += rom_num[i]
				num -= int_num[i]
				print(num)
			i += 1
		return roman_num


print(Roman_num().int_converter_Rom(10*10-9))


