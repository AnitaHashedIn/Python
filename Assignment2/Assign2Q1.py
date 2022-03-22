
# 2a. Write a program to input an integer N from user and print pascal triangle up to N rows.
#
# input - 3
#
# Output 1:
#
# 1 0 0
#
# 1 1 0
#
# 1 2 1



from math import factorial

# input n
n = 5
for i in range(n):
    for j in range(i + 1):
        # nCr = n!/((n-r)!*r!)
        print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
    for j in range(n - i -1):
        # for right 0
        print(0,end=" ")
    # for new line
    print()