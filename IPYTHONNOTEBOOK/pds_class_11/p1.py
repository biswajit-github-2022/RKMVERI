import sys
def f1():
    return "hello world"
def f2():
    return "good morning"
if __name__=='__main__':
    f1()
    f2()
    print(sys.argv[1])