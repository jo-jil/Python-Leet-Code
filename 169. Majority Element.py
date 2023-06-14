class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x = Counter(nums)
        r = x.most_common(1)
        return r[0][0]
