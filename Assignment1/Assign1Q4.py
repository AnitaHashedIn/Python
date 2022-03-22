# Keys = [‘Ten’, ‘Twenty’, ‘Thirty’]
# Value = [10,20,30]
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
Keys = ['Ten', 'Twenty', 'Thirty']
Value = [10, 20, 30]

d={}
if len(Keys) == len(Value):
    for i,j in zip(Keys,Value):
        d[i] = j
    print(d)
else:
    print("Can not be mapped")