# Question 1

def f1(a : int,b : float) -> float:
    """
    This functon accepts two parameters first is int type and second is float type and returns a float type
    """
    return a+b

def f2(a: int,b : int, c : str = '-') -> str:
    """
    This functon accepts three parameters first two are int type and third is string type with a default value
    '-' 
    It returns a string type
    """
    return str(a) + c + str(b)

#print(f1(1))
print(f'{"-"*10}1{"-"*10}')
print(f1(1,2))
print(f'{"-"*10}2{"-"*10}')
print(f1(1,2.3))
print(f'{"-"*10}3{"-"*10}')
print(f1(a=1,b=2))
print(f'{"-"*10}4{"-"*10}')
print(f1(a=1,b=2.3))
print(f'{"-"*10}5{"-"*10}')
#print(f1(1,2,3))
print(f'{"-"*10}6{"-"*10}')
#print(f1(1,a=1))
print(f'{"-"*10}7{"-"*10}')
#print(f1(1,c=2))
print(f'{"-"*10}8{"-"*10}')
print(f1(1,b=2))
print(f'{"-"*10}9{"-"*10}')
print(f1(1,b=2.3))
print(f'{"-"*10}10{"-"*10}')
print(f1(1.1,2.3))

def deco_func1(f):
    """
    This function decorates the function f1 for parameter validation
    """
    def inner_func(*args,**kwargs):
        # your program goes below ---->>>>>
        # develop this function such the when the commented lines are uncommented one by one they
        # display the corresponding error as indicated in the respective comments
        # you will need to work by manually raising Exceptions with the corressponding messages
        # delete the pass statement below and write your own program here
        pass
    return inner_func

f1 = deco_func1(f1)

#print(f1(1)) # if uncommented gives message "Exception: function : f1 has not been supplied the correct number of parameters"
print(f'{"-"*10}1{"-"*10}')
#print(f1(1,2))  # if uncommented gives message "Exception: function : f1 has not been supplied parameters of proper type"
print(f'{"-"*10}2{"-"*10}')
print(f1(1,2.3))
print(f'{"-"*10}3{"-"*10}')
#print(f1(a=1,b=2))  # if uncommented gives message "Exception: function : f1 has not been supplied parameters of proper type"
print(f'{"-"*10}4{"-"*10}')
print(f1(a=1,b=2.3))
print(f'{"-"*10}5{"-"*10}')
#print(f1(1,2,3))  # if uncommented gives message "Exception: function : f1 has not been supplied parameters of proper type"
print(f'{"-"*10}6{"-"*10}')
#print(f1(1,a=1))  # if uncommented gives message "Exception: function : f1 has not been supplied the correct keyword parameter"
print(f'{"-"*10}7{"-"*10}')
#print(f1(1,c=2))  # if uncommented gives message "Exception: function : f1 has not been supplied the correct keyword parameter"
print(f'{"-"*10}8{"-"*10}')
#print(f1(1,b=2))  # if uncommented gives message "Exception: function : f1 has not been supplied parameters of proper type"
print(f'{"-"*10}9{"-"*10}')
print(f1(1,b=2.3)) 
print(f'{"-"*10}10{"-"*10}')
#print(f1(1.1,2.3))  # if uncommented gives message "Exception: function : f1 has not been supplied parameters of proper type"
print(f'{"-"*10}11{"-"*10}')
print(f1(b=2.3,a=1))
print(f'{"-"*10}12{"-"*10}')
print(f1(1,2.3,3,4))

# Question 2
#
# write a similar decorator function for the function f2 such that all wrong actual parameters are handled and suitable
# messages are displayed by raising Exceptions
# Ensure there are test cases for the following situations - usage of default value for the third parameter; 
# usage of non-default value for the third parameter and for usage of non-string value for the third parameter (which
# should raise suitable messaged exception)

# Question 3
#
# write class decorators for the above decoration for both f1 and f2








                    