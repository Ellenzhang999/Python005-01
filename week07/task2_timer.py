import datetime

def timer(func):
    def inner2(*args,**kwargs):
        start_time = datetime.datetime.now()
        func(*args,**kwargs)
        end_time = datetime.datetime.now()
        duration = (end_time - start_time).microseconds
        print(f"it costs {duration} microseconds")
    return inner2

@timer
def f1(n):
    for i in range(n):
        pass

f1(10000)

@timer
def f2(a,b):
    for i in range(a):
        for j in range(b):
            pass

f2(10000,10000)