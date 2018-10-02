class Circle:

	def __init__(self, r):
		self.r = r

	def area(self):
		return self.r**2*3.14

	def perimeter(self):
		return self.r*2*3.14



class Square:

	def __init__(self, x):
		self.x = x

	def area(self):
		return self.x**2

	def perimeter(self):
		return self.x*4







My_Circle = Circle(6)
print(My_Circle.area())
print(My_Circle.perimeter())

My_Square = Square(5)
print(My_Square.area())
print(My_Square.perimeter())