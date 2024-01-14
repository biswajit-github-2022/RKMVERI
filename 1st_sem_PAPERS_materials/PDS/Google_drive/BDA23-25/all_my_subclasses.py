import all_my_classes as amc

class my_subclass(amc.my_class):
	"""
	This is a sublcass of my_class imported from the all_my_classes module
	This demonstrates the creation and usage of subclasses (inheritance) in python
	"""

	def __init__(self,param1,param2,param3):
		self._instance_var3 = param3
		super().__init__(param1,param2)
		
		
	def instance_method3(self):
			""" overriding superclass instance_method3 """
			print(f'overriden instance method 3 output: {self._instance_var1 - self._instance_var2}')

	def instance_method4(self,param1):
			""" new instance method of the subclass """
			self._instance_var3 += param1

	def __str__(self):
			return f'No. of instances created : {my_subclass.a_class_var} instance var1: {self._instance_var1} instance var2: {self._instance_var2} instance var3: {self._instance_var3}'


if __name__ == '__main__':
	o1 = my_subclass(1,100,200)
	print(my_subclass.a_class_var)
	o2 = my_subclass(-1,-100,300)
	print(my_subclass.a_class_var)

	o3 = amc.my_class(2,200)
	print(amc.my_class.a_class_var)

	print(o1)
	print(o2)
	print(o3)

	o1.instance_method1(3)
	o3.instance_method1(3)

	print("-"*20)
	print(o1)
	print(o3)
	
	o1.instance_method3()
	o3.instance_method3()
	o1.instance_method4(5)



	
