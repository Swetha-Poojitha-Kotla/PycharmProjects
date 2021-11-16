#to fecth value one at a time
# iterator preserve value of old values
nums = [7, 8, 9, 2, 7, 3, 3, 4, 9, 6, 8, 9, 5, 4, 3]

# for i in nums:
#     print(i)

it = iter(nums)
print(it.__next__())
# print(it.__next__())
# print(it.__next__())

print(next(it))


class Topten:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num = self.num + 1

            return val
        else:
            raise StopIteration

vals = Topten()
# print(next(vals))
for i in vals:
    print(i)
