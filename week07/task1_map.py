
def my_map(func,*iterators):
    if not iterators:
        raise TypeError('Mapper should have at least two parameters')
    try:
        i = 0
        while True:
            # print(i)
            yield func(*[j[i] for j in iterators])
            i+=1
    except IndexError:
        pass

# map(lambda a: a + 200, li)

# test：一个list
def f1(a):
    return a + 100

l1 = [11, 22, 33, 44, 55]
result = my_map(f1, l1)
print(list(result))

# test2: 多个list
f2=lambda x,y:x==y
l2=[1,2,44,4,5,6,7,8,9]
l3=[1,2,3,4,11,6,7,8,9]
print(list(my_map(f2,l2,l3)))

# test3: error
print(list(my_map(f1)))
# TypeError: Mapper should have at least two parameter
