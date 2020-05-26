#1st task
class Circle(object):	
	"""docstring for Circle"""
	def __init__(self, radius, color):
		super(Circle, self).__init__()
		self.radius = radius
		self.color = color
	
		if not (isinstance(radius, int) or isinstance(radius, float)):
			raise Exception("Sorry, wrong type of variable")

		if not isinstance(color, str):
			raise Exception("Sorry, wrong type of variable")

	def print(self):
		return ("A " + self.color + " circle with radius " + str(self.radius))

	def area(self):
		import math
		area = math.pi * self.radius * self.radius
		return area

	def circ(self):
		pi = 3.14
		circ = 2 * pi * self.radius
		return circ


c1 = Circle(5.2, "red")
print(c1.print()) 
print(c1.area())
print(c1.circ())


#2nd task
class Roman_Int:

    def __init__(self, num):
        self.roman_num = num


    def int_to_Roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num
    def from_roman(self, num):
        roman_numerals = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0
        for i,c in enumerate(num):
            if (i+1) == len(num) or roman_numerals[c] >= roman_numerals[num[i+1]]:
                result += roman_numerals[c]
            else:
                result -= roman_numerals[c]
        return result



    def add_roman(self, x):
        return Roman_Int(self.int_to_Roman(self.from_roman(self.roman_num) + x.from_roman(x.roman_num)))


    def sub_roman(self, y):

        if self.from_roman(self.roman_num) >= y.from_roman(y.roman_num):
            return Roman_Int(self.int_to_Roman(self.from_roman(self.roman_num) - y.from_roman(y.roman_num)))
        else:
            raise Exception("Sorry, cannot share negative values")
        

    def div_roman(self, z):

        if z.from_roman(z.roman_num) > 0:
            return Roman_Int(self.int_to_Roman(self.from_roman(self.roman_num) // z.from_roman(z.roman_num)))
        else:
            raise Exception("Sorry, cannot share inf or negative values")


    def mult_roman(self, k):
        return Roman_Int(self.int_to_Roman(self.from_roman(self.roman_num) * k.from_roman(k.roman_num)))


    def sq_roman(self, j):
        return Roman_Int(self.int_to_Roman(self.from_roman(self.roman_num) ** j.from_roman(j.roman_num)))


    def __str__(self):
        return self.roman_num




a = Roman_Int("I")
b = Roman_Int("")
print(a.add_roman(b))
print(a.from_roman("X"))
print(b.int_to_Roman(5))
print(a.sub_roman(b))
print(a.div_roman(b))
print(a.mult_roman(b))
print(a.sq_roman(b))


#3rd task
class Person(object):
	"""docstring for Person"""
	def __init__(self, name, last_name, age, gender, student, password):
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

	def Password(self, password):
		self._password = password	
		return ("Password is " +  "*" * len(password) + " and is hidden!")


	def Goodbye(self):
		print("Bye everyone!")

	def Favourite_num(self, num1):
		return ("My favorite number is " + str(num1))


	def Read_file(self, filename):
		try:
			open(f"{filename}.txt")
		except FileNotFoundError:
			return ("no file found")
			


p1 = Person("John", "Smith", 25, "M", "Tutor", "YouSHallNotPass!")
print(p1.Favourite_num(5))
p1.Greeting("Jane")
print(p1.Position(1))
print(p1.Password("YouSHallNotPass"))
print(p1.Read_file("testing"))


#4rth task
