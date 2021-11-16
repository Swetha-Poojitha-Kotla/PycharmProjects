nums = [5,4,6,7,8,23,46,78,10]

def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]

sort(nums)
print(nums)
