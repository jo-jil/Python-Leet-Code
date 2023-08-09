class Solution:
    def climbStairs(self, n: int) -> int:
        a = [0 for x in range(n)]
        for i in range(n+1):
            if i == 1:
                a.insert(i, 1)
            elif i == 2:
                a.insert(i, 2)
            elif i == 3:
                a.insert(i, 3)
            if i > 3:
                a.insert(i, a[i-2]+a[i-1])
        return a[n]
