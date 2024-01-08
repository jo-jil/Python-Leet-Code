class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for n in range(len(nums)):
            if nums[n] in map:
                return True
            map[nums[n]] = n
        return False
