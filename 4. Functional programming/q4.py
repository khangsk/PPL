# a)
def compose(*arg):
    if len(arg) == 1: return lambda x: arg[0](x)
    return arg[0](compose(*arg[1:]))
    

def double(x):
    return x * 2
def increase(x):
    return x + 1
def square(x):
    return x * x
a = compose(square, increase, double)
print(a(3))
# b)
# from functools import reduce
# def compose(*arg):
#     def a(x):
#         return reduce(lambda x, y: y(x), arg, x)
#     return a

# def double(x):
#     return x * 2
# def increase(x):
#     return x + 1
# def square(x):
#     return x * x
# a = compose(square, increase, double)
# print(a(3))

