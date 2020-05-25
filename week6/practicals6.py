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
