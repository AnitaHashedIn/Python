# 1.	Return all the duplicate values from list of arraylist
# Input:
# [[1,1,3,2],[9,8,8,1],[0,4,5,0,0,1,4]]
# Output:
# 1 -> 2
# 8 -> 2
# 0 -> 3, 4 -> 2


a = [[1, 1, 3, 2], [9, 8, 8, 1], [0, 4, 5, 0, 0, 1, 4]]
# result dictionary for repeated numbers
ResMap ={}
for i in a:
    d = {}
    for j in i:
        if j not in d:
            d[j] =1
        else:
            d[j] += 1
        if d[j]>1:
            ResMap[j] = d[j]

# output
for i in ResMap:
    print(i, " -> ", ResMap[i])

