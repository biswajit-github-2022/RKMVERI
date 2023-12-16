class my_list(list):
    """
    This inherits from the built-in class list and overrides three of its methods
    - initialization (works with no parameters), 
    - add (allows only same length numeric lists to be added), 
    - append (allows only numeric elements to be added to a list)
    """
    def __init__(self,an_iterable=None):
        if an_iterable is None:
            super().__init__()
        else:
            super().__init__(an_iterable)

    def __add__(self,l2,mode='m'):
        if mode != 'm':
            return super().__add__(l2)
        if isinstance(l2,list):
            if len(self) == len(l2):
                if all([isinstance(x,(int,float)) for x in self]) and all([isinstance(x,(int,float)) for x in l2]):
                    l_temp = []
                    for i in range(len(self)):
                        l_temp.append(self[i] + l2[i])
                else:
                    raise Exception('The list elements are not numeric')
            else:
                raise Exception('The list lengths are not compatible')
        else:
            raise Exception('The parameter supplied is not a list')
        return l_temp
    
    def append(self, __object: int) -> None:
        if isinstance(__object, int):
            super().append(__object)
        else:
            raise Exception('Element to be appended is not int type')
                
if __name__ == '__main__':
    l1 = my_list([2,3,4])
    l2 = my_list([1,-3,7])
    print(l1+l2) # should print [3, 0, 11]
    #l1.append(2.3)  # raises Exception giving message that the element is not int type
    l1.append(2)
    print(l1) # should print [2, 3, 4, 2]
    #l2 = ['a','b','c']
    #print(l1+l2)  # raises Exception giving message that the list elements are not numeric
    #l2 = [1,2,3,4]
    #print(l1+l2)  # raises Exception giving message that the list lengths are not compatible
    #l2 = (1,2,3)
    #print(l1+l2) # raises Exception giving message that the parameter supplied is not a list
    l1 = my_list() # works when no parameter supplied
    print(l1) # prints an empty list
    l1 = my_list([2,3,4])
    print(l1.__add__(['a','b','c'],mode='x')) # should print [2, 3, 4, 'a', 'b', 'c']
    l3 = [1,2,3]
    print(l1.__add__(l3,'a')) # should print [2, 3, 4, 1, 2, 3]

    


