def f1(x,y,z,a):
	return (x+2*y+z) % a == 0

print(f1(1,2,3,2))

def deco_func1(f):
	def inner_func(*args,**kwargs):
		if 'a' not in kwargs.keys():
			raise Exception('parameter a not supplied!')
		return f(args[0],args[1],args[2],kwargs['a'])
	return inner_func

@deco_func1
def f1(x,y,z,a):
	return (x+2*y+z) % a == 0

def f2(x,y,z,a):
	return (x+2*y+z) % a == 0

def deco_func2(f):
	def inner_func(*args,**kwargs):
		if 'a' not in kwargs.keys():
			a = 2
		else:
			a = kwargs['a']
		return f(args[0],args[1],args[2],a)
	return inner_func



def f2(x,y,z,a):
	return (x+2*y+z) % a == 0

f2 = deco_func2(f2)


if __name__ == '__main__':
	try:
		print(f1(1,2,3,2)) # will raise an exception
	except Exception as e:
		print(e)	
	print(f1(1,2,3,a=2))
	print(f2(1,2,3))
	