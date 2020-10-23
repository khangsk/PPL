def dist(lst, n):
    if len(lst) == 0: return []
    return [(lst[0],n)] + dist(lst[1:],n)
print(dist([],3))