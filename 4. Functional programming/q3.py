from functools import reduce
def lessThan(n, lst):
# a)    
    # return [x for x in lst if x < n]

# b)    # if len(lst) == 0: return []
    # if lst[0] < n: return [lst[0]] + lessThan(n,lst[1:])
    # else: return lessThan(n,lst[1:])

# c)
    return list(reduce(lambda x, y: [x, y] if x < n else y, lst))
    
print(lessThan(50, [1, 55, 6, 2]))