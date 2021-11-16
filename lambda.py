#passing function to function
def square(a):
    return a*a

res = square(10)
print(res)


f = lambda a,b:a*b
res = f(5,6)
print(res)

