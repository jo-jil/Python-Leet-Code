class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, n in enumerate(nums):
            if (target - n) in dict:
                return [dict[target-n], i]
            dict[n] = i
