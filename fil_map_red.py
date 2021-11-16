from functools import reduce
nums = [1,2,3,4,76,6,7,8,3,24,5,5,6,86]

def add_all(a,b):
    return a+b
def is_even(n):
    return n%2==0
evens = list(filter(is_even,nums))
print(evens)

odds = list(filter(lambda n : n%2!=0,nums))
print(odds)

doubles = list(map(lambda n : n*2,evens))
print(doubles)

sum = reduce(lambda a,b:a+b, doubles)
print(sum)