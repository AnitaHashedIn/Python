# 2. Create a generator to return the fibonnaci sequence starting from the first element
#
# up to (n). The first numbers of the sequence are: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,
#
# 89, . . .

def myGenerator(n):
    a = 0
    b = 1
    yield a
    yield b
    for i in range(n):
        c = a+b
        a,b = b,c
        yield c
n = int(input())
fib = myGenerator(n)
for i in range(n*n):
    print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))

