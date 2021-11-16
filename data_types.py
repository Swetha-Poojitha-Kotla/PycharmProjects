#None -> whe variable is not assigned to vany values instead of NULL
# Numeric -> int, float, complex, bool
#Sequence -> List, Tuple, Set, String, Range
#Dictionary

from ins import print, int, type

num = 2.5
print(type(num))
num = 3
print(type(num))
num = 6+9j
print(type(num))
a= 5.6
b = int (a)
print(type(b))
k = float(b)
print(type(k))
c = complex(b,a)
print(c)
print(b>k)
print(int(True))

print(list(range(10)))
print(set(range(10)))
print(tuple(range(10)))


#print even numbers from 1 - 20
print(list(range(1,10,5)))

