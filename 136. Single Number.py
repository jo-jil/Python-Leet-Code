class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count_map = {}
        for item in nums:
            if item in count_map:
                count_map[item] += 1
            else:
                count_map[item] = 1
        value_with_count_1 = None
        for item, count in count_map.items():
            if count == 1:
                value_with_count_1 = item
                break

        return value_with_count_1
