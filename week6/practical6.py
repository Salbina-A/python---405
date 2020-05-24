class Circle(object):	
	"""docstring for Circle"""
	def __init__(self, radius, color):
		super(Circle, self).__init__()
		self.radius = radius
		self.color = color
		check_radius = isinstance(radius, int)
		check_color = isinstance(color, str)
		if not check_radius:
			raise Exception("Sorry, wrong type of variable")

		if not check_color:
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


c1 = Circle(5, "red")
print(c1.print()) 
print(c1.area())
print(c1.circ())
