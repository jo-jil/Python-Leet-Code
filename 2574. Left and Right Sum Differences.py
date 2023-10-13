class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = nums.copy()
        right = nums.copy()  
        ans = nums.copy()

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                right[i] += nums[j]
            right[i] = right[i] - nums[i]
        right[len(nums)-1] = 0

        for i in range(1, len(nums)):
            for j in range(i):
                left[i] += nums[j]
            left[i] = left[i] - nums[i]
        left[0] = 0

        for i in range(len(nums)):
            ans[i] = abs(right[i] - left[i])
        return ans
