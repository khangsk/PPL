from functools import reduce
def flatten(lst):
# a)
    # return [y for x in lst for y in x]

# b)    # if len(lst) == 0: return []
    # return lst[0] + flatten(lst[1:])

# c)    
    return reduce(lambda x,y: x + y, lst, [])

print(flatten([[1,2,3],['a','b','c'],[1.1,2.1,3.1]]))