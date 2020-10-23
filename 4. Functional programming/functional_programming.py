###########           FUNCTIONAL PROGRAMMING
# 1> Immutable data types in Python
#   Number, bool, string, sequence (tuple, range)
#       x = frozenset({1,'a',True})

# a = b = [1,2,3]
# a.extend([4,5])
# print(a, b)

# 2> Lambda function
#  2.1> Anonymous function
#   lambda parameter_list: expression
#    parameter_list: any number of parameters
#    expression: only one expression
    # s = lambda x, y: x + y
    # print(s(3,4))
#  2.2> First-class function
    # def foo(a, b): pass
    # x = foo
    # x(3,4)

    # def foo(f, x):
    #     return f(x)
    # print(foo(lambda a: a ** 2, 4))

    # def f(x):
    #     def g(y):
    #         return x * y
    #     return g
    # m = f(3)
    # print(m(4), f(3)(4))

# 3> High-order functions: map, filter, reduce
#   3.1> map(<function>,<sequence>)
#       print(list(map(lambda a, b: a + b, [1,2,3],[7,8,9])))
#   3.2> filter(<function>,<sequence>)
#       print(list(filter(lambda x: x % 2 == 0, [1,2,3,4,5,6,7,8])))
#           parameter of map and filter: 1, 2,... parameter
#   3.3> reduce(<function>,<sequence>,<initial>?)
#           parameter of reduce: at least 1 parameter
        # from functools import reduce
        # sequence = [2, 9, 6]
        # # ((1 * 2) * 9) * 6 = 216
        # print(reduce(lambda a, b: a * b, sequence, 1)) 

        # from functools import reduce
        # from abc import ABC 
        # class Exp(ABC): pass
        # class IntLit(Exp): pass
        # class BinLit(Exp): pass
        # exp = [12, ("+", 23), ("-", 14)]
        # reduce(lambda acc, ele: BinLit(ele[0], acc, IntLit(ele[1])), exp[1:], IntLit(exp[0]))
        # # same: 
        # acc = IntLit(exp[0])
        # for ele in exp[1:]:
        #     acc = BinLit(ele[0], acc, IntLit(ele[1]))
# # 4> Closure
    # def power(y):
    #     def inner(x):
    #         return x**y
    #     return inner
    # square = power(2)
    # print(square(5))
# def log_decorator(func):
#     def inner(*arg):
#         print(func.__name__+" is running")
#         return func(*arg)
#     return inner
# @log_decorator
# def foo(x, y):
#     return x*y
# print(foo(3,4))

# def dist(a,n1):
#     if n1:
#         n2 = dist(a,n1[1:])
#         n2.insert(0,(a,n1[0]))
#         return n2
#     else:
#         return []
# print(dist(2,[3,4,5]))

def lessThan(lst,n):
    return list(filter(lambda x: x < n,lst))

print(lessThan([1,2,3,4,5],4))

# def flatten(lst):
#     if len(lst) == 0: return []
#     return lst[0] + flatten(lst[1:])

# print(flatten([[1,2,3],[4,5],[6,7]]))