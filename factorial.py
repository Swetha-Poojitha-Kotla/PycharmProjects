def fact(x):
    f =1
    for i in range(1,x+1):
        f = f*i
    return f

res = fact(4)
print(res)