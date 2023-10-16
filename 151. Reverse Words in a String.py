class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        for word in reversed(s.split()):
            ans += word + " "
        ans = ans[:-1]
        return ans
