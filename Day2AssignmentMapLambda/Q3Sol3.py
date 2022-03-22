# 3. Convert a number to positive if it's negative in the list. Only pass those that are converted from negative
# to positive to the new list.
# lst1=[-1000, 500, -600, 700, 5000, -90000, -17500]
lst1=[-1000, 500, -600, 700, 5000, -90000, -17500]

def filterNegatives(item):
    if item<0:
        return True
    return False

def NegToPos(item):
    return -1*item

res = list(map(NegToPos,list(filter(filterNegatives,lst1))))

print(res)