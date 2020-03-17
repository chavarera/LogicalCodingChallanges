from abc import ABC ,abstractmethod

class Shape(ABC):
	@abstractmethod
	def area(self):
		pass

	@abstractmethod
	def perimeter(self):
		pass

class Square(Shape):
	def __init__(self,side):
		self.side = side

	def area(self):
		return self.side * self.side

	def perimeter(self):
		return 4 * self.side

s1 = Square(5)



s2= Square(4)

print(s1.area())
print(s1.perimeter())

