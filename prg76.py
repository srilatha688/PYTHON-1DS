def swap_by_value(nums):
      nums[0],nums[1]=nums[1],nums[0]
nums=[10,20]
print("before swap:nums=",nums)
swap_by_value(nums)
print("after swap:nums=",nums)
