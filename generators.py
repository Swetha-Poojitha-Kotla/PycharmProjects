#generators ill give iterators

def topTen():

    n = 1
    while n<=10:
        sq = n*n
        yield sq
        n+=1




vals = topTen()
# print(vals.__next__())
# print(vals.__next__())
# print(vals.__next__())
# print(vals.__next__())


for i in vals:
    print(i)
