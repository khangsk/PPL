def double(lst):
# a)    # a = []
    # return [x * 2 for x in lst]

# b)    
    # if len(lst) == 0: return []
    # return [lst[0] * 2] + double(lst[1:])
    
# c)    
    return list(map(lambda x: x * 2, lst))
print(double([5,7,12,-4]))    
