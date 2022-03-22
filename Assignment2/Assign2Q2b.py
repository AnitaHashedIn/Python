# 2
# b.Write
# a
# program
# to
# print
# the
# following
# pattern
#
# *
#
# ** *
#
# ** ** *
#
# ** ** ** *
#
# ** ** ** ** *
#
# ** ** ** *
#
# ** ** *
#
# ** *
#
# *



n = 5
a = 1
d =2

for i in range(n):
    j = a+(i-1)*d

    for l in range (2*(n-i)):
        print(" ",end="")

    for k in range(j):
        print("*", end="")
    print()
for i in range(n,-1,-1):
    j = a+(i-1)*d
    for l in range (2*(n-i)):
        print(" ",end="")

    for k in range(j):
        print("*", end="")
    print()