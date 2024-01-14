class my_class:
	"""
	This is the documentation for my_class
	This class has two instance variables and one class variable
	This class has two instance methods
	"""
	
	a_class_var = 0
	
	def __init__(self, param1, param2):
		"""
		the instance variables are initialized, class variable updated and instance created
		"""
		self._instance_var1 = param1
		self._instance_var2 = param2
		my_class.a_class_var += 1

		print('initialization of the instance variables done, an instance of the class created')

	def instance_method1(self,param1):
		"""
		the doc for instance_method1
		"""
		self._instance_var1 += param1
		return self._instance_var1

	def instance_method2(self,param1):
		self._instance_var2 += param1
		return self._instance_var2

	def instance_method3(self):
		print(f'instance method 3 output: {self._instance_var1 + self._instance_var2}')

	def __str__(self):
		return f'No. of instances created : {my_class.a_class_var} instance var1: {self._instance_var1} instance var2: {self._instance_var2}'

if __name__ == '__main__':
	o1 = my_class(1,100)
	print(my_class.a_class_var)
	o2 = my_class(-1,-100)
	print(my_class.a_class_var)
	o3 = my_class(2,200)
	print(my_class.a_class_var)
	print(o1)
	print(o2)
	o1.instance_method1(3)
	o1.instance_method2(3)
	print(o1)
	print(my_class.__doc__)
	print(o1.__doc__)
	print(o1.__init__.__doc__)
	print(o1.instance_method1.__doc__)
	

	



		