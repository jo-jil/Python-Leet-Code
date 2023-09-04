class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = self.rever(s)

        if t == t[::-1]:
            return True

        return False

    def rever(self, s: str) -> str:
        str = ""
        for i in s.lower():
            if i.isalpha() or i.isnumeric():
                str+=i
        return str
