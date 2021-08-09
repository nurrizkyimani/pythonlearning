import copy

org = [[1,2,4,5], [2,4,4,5]]
cpy = copy.deepcopy(org)

cpy[0][1] = -100

print(org)
print(cpy)