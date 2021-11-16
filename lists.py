nums = [12,2,3,4,55,67,6,7,123]
print(nums)
print(nums[5])
print(nums[3:6])
print(nums[-1])
print(nums[-9])

names = ['my','name','is','swetha','poojitha']
print(names)
names.append('abhi')
print(names)
values=[1,'swetha','67.5']
print(values)
#spl way to store lists
mix = [nums,names,values]
print(mix)

#difference between insert and append -> insert given index element is added, append -> add at end
#diff between remove and pop - remove -> directly removes element and pop - given index will remove that element
#pop without index -> last element is removes
names.pop(4)
print(names)

del nums[2:5]
print(nums)

#mathematical functions
print(min(nums))
print(sorted(names))