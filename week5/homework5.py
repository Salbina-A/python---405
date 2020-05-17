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

#2nd task
class Person(object):
	def __init__(self, name, last_name, age, gender, student):
		super(Person, self).__init__()
		self.name = name
		self.last_name = last_name
		self.age = age
		self.gender = gender
		self.student = 0


	def Greeting(self, second_person):
		print("Welcome dear " + second_person + "\n Best,\n" + self.last_name)

	def Position(self, student):
		if student == 1:
			return True
		else:
			return False

	def Goodbye(self):
		print("Bye everyone!")

	def Favourite_num(self, num1):
		return ("My favorite number is " + str(num1))
	

p1 = Person("John", "Smith", 25, "M", "Tutor")
print(p1.Favourite_num(5))
p1.Greeting("Jane")
print(p1.Position(1))


