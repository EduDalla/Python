def func_1(a):
    return a ** a


def func_2(a): # func_2(a) also turns func_1(a) == 2
    return func_1(a) * func_1(a)


print(func_2(2)) # 16
