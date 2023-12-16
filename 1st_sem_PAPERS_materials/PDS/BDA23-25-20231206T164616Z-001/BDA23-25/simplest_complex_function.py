def f1(x,y,z,a=10,b=20,*args,**kwargs):
    print(f'x: {x} y: {y} z: {z} a: {a} b: {b} {args} {kwargs}')
    print(len(args))
    for k,v in kwargs.items():
        print(f'k: {k} v: {v}')


#f1(2,3,4,5,6,7,8,**{'a1':1,'b1':2})
f1(2,3,4,5,6,7,8,*(9,10),**{'a1':1,'b1':2})