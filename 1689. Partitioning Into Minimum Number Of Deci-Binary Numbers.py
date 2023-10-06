class Solution:
    def minPartitions(self, n: str) -> int:
        digits = [int(digit) for digit in n]
        highest_digit = max(digits)
        return highest_digit
