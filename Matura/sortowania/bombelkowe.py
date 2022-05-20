nums = [7,55,37,83564,22,1,4,99,14]

for i in range(len(nums)-1):
    for j in range(len(nums)-1-i):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
print(nums)