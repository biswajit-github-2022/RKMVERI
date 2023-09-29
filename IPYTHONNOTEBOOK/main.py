import time 


def deco_func(f):
    def inner_func():
        t1=time.time()
        f()
        t2=time.time()
        return f"time taken to exc f ={t2-t1}"
    return inner_func


@deco_func
def f():
    return "hi"
