import sys

sys.setrecursionlimit(10)
print(sys.getrecursionlimit())
i = 0
def greet():
    global i
    i = i+1
    print("hello",i)
    greet()


def fact(x):
    if x==0:
        return 1
    return x*fact(x-1)


result = fact(4)
print(result)