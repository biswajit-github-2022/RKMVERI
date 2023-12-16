# Question 4

class my_list(list):
    """
    This inherits from the built-in class list and overrides three of its methods
    - initialization (works with no parameters), 
    - add (allows only same length numeric lists to be added), 
    - append (allows only numeric elements to be added to a list)
    """
    def __init__(self,an_iterable=None):
        # your code here after you delete the dummy pass statement below
        if an_iterable is None:
            super().__init__()
        else:
            super().__init__(an_iterable)

    def __add__(self,l2,mode='m'):
        # your code here after you delete the dummy pass statement below -
        # If the mode is 'm' meaning "modified" which is also the default value for this parameter 
        # then you give the sum of the corresponding int elements, else for mode value anything else
        # use the default concatenation operation of the super class
        if mode=="m":
            for i in l2:
                if type(i)!=int:
                    raise Exception("list elements are not numeric")
                # if
            return sum(l2)
        else:
            super.__add__(l2)
    
    def append(self, __object: int) -> None:
        # your code here after you delete the dummy pass statement below
        pass
                
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

    


# sol.
# Question 4

# class my_list(list):
#     """
#     This inherits from the built-in class list and overrides three of its methods
#     - initialization (works with no parameters),
#     - add (allows only same length numeric lists to be added),
#     - append (allows only numeric elements to be added to a list)
#     """

#     def __init__(self, an_iterable=None):
#         # your code here after you delete the dummy pass statement below
#         if an_iterable is None:
#             super().__init__()
#         else:
#             super().__init__(an_iterable)

#     def __add__(self, l2, mode='m'):
#         # your code here after you delete the dummy pass statement below -
#         # If the mode is 'm' meaning "modified" which is also the default value for this parameter
#         # then you give the sum of the corresponding int elements, else for mode value anything else
#         # use the default concatenation operation of the super class
#         if not isinstance(l2,list):
#             raise Exception("the parameter supplied is not a list")
#         else:
#             if mode=='m':
#                 for i in l2:
#                     if(type(i)!=int):
#                         raise Exception("the list elements are not numeric")
#                         break
#                 if len(l2)!=len(self):
#                     raise Exception("the list lengths are not compatible")
#                 else:
#                     return  [self[i]+l2[i] for i in range(len(self))]
#             else:
#                 return super().__add__(l2)



#     def append(self, __object: int) -> None:
#         # your code here after you delete the dummy pass statement below
#         if type(__object)!=int:
#             raise Exception ("element is not int type")
#         else:
#             super().append(__object)


# if __name__ == '__main__':
#     l1 = my_list([2, 3, 4])
#     l2 = my_list([1, -3, 7])
#     print(l1 + l2)  # should print [3, 0, 11]
#     # l1.append(2.3)  # raises Exception giving message that the element is not int type
#     l1.append(2)
#     print(l1)  # should print [2, 3, 4, 2]
#     #l2 = ['a','b','c']
#     #print(l1+l2)  # raises Exception giving message that the list elements are not numeric
#     #l2 = [1,2,3]
#     #print(l1+l2)  # raises Exception giving message that the list lengths are not compatible
#     # l2 = (1,2,3)
#     # print(l1+l2) # raises Exception giving message that the parameter supplied is not a list
#     l1 = my_list()  # works when no parameter supplied
#     print(l1)  # prints an empty list
#     l1 = my_list([2, 3, 4])
#     print(l1.__add__(['a', 'b', 'c'], mode='x'))  # should print [2, 3, 4, 'a', 'b', 'c']
#     l3 = [1, 2, 3]
#     print(l1.__add__(l3, 'a'))  # should print [2, 3, 4, 1, 2, 3]