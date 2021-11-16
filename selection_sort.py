nums = [5, 4, 6, 7, 8, 23, 46, 78, 10]


def select_sort(nums):
    for i in range(8):
        min = i
        for j in range(i, 9):
            if nums[j] < nums[min]:
                min = j
        nums[i], nums[min] = nums[min], nums[i]


select_sort(nums)
print(nums)
