# 1.write a decorator which will take a function and execute it twice.
#
# Function is -
#
# def multiply(num1, num2):
#
#     print(num1 * num2)

def Mul_Decorator(func):

    def wrap_func(*args,**kargs):
        # print('before')
        func(*args, **kargs)
        func(*args, **kargs)
        # print('after')
    return wrap_func

@Mul_Decorator
def multiply(a,b):
    print(a*b)

multiply(4,5)
