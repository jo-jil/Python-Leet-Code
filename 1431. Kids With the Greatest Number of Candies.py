class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        high = max(candies)
        print(high)
        ans = []
        for i in candies:
            if((i + extraCandies) >= high):
                ans.append(True)
            else:
                ans.append(False)
        return ans
