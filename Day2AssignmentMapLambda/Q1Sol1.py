# 1. Using a lambda function take inputs as 4 integers and give the output for equation ax^2+bx+c

a,b,c,x = 1,2,3,4

res = lambda a,b,c,x: a*(x**2)+b*x+c

print(res(a,b,c,x))