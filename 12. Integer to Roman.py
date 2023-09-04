import math
class Solution:
    def intToRoman(self, num: int) -> str:
        print(num)
        ans = ""
        if (num > 999):
            x = num/1000
            for i in range (0,math.floor(x)):
                ans = ans + "M"
            num = num%1000
        
        if (num > 899):
            ans = ans + "CM"
            num = num%900
        
        if (num >499):
            ans = ans + "D"
            num = num%500

        if (num > 399):
            ans = ans+ "CD"
            num = num%400
        
        if (num >99):
            x = num/100
            for i in range (0,math.floor(x)):
                ans = ans + "C"
            num = num%100

        if(num > 89):
            ans = ans + "XC"
            num = num%90
        
        if (num >49):
            ans = ans + "L"
            num = num %50
        
        if (num > 39):
            ans = ans + "XL"
            num = num%40
        
        if (num > 9):
            x = num/10
            for i in range (0,math.floor(x)):
                ans = ans + "X"
            num = num%10
        
        if(num == 9):
            ans = ans + "IX"
            num = num%9
        
        if (num > 4):
            ans = ans + "V"
            num = num%5

        if (num == 4):
            ans = ans + "IV"
            num = num%4
        
        if(num >0):
            x = num
            for i in range (0,x):
                ans = ans + "I"
            num = num%1

        return ans
