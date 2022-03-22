# 7.	Convert Dictionary to list
# The original dictionary is : {‘HuEx: [1, 3, 4], ‘is’: [7, 6], ‘best’: [4, 5]}
# The converted list is : [[‘HuEx, 1, 3, 4], [‘is’, 7, 6], [‘best’, 4, 5]]
d = {"HuEx": [1, 3, 4], "is": [7, 6], "best": [4, 5]}
res = [ [k,v] for k,v in d.items()]
print(res)