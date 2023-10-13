def convert_to(number, base):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result

def pal(num) -> bool:
    if num == num[::-1]:
        return True
    else:
        return False

class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, n - 1):  # Changed the range to correct the loop bounds
            if (pal(convert_to(n,i))) == False:
                return False
        return True
