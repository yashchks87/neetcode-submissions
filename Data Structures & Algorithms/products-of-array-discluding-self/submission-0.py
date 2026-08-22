class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_val, right_val = 1, 1
        left, right = [1] * len(nums), [1] * len(nums)
        for x in range(len(nums)):
            left[x] *= left_val
            left_val *= nums[x]
        for x in range(len(nums)-1, -1, -1):
            right[x] *= right_val
            right_val *= nums[x]
        return [x * y for x, y in zip(left, right)]