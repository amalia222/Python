nums = list(map(int, input().split()))
i1 = nums.index(max(nums))
i2 = nums.index(min(nums))
nums[i1], nums[i2] = nums[i2], nums[i1]
print(*nums)
