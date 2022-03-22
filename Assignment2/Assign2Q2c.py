
n = 19
a = 1
d =2

for i in range(n):
    j = a+(i-1)*d

    for l in range ((n-i-1)):
        print(" ",end="")

    print("*",end="")
    for k in range(j):
        if(i==n-1):
            print("*",end="")
        else:
            print(" ", end="")
    if(i!=0):
        print("*",end="")
    print()