class Solution:
    def palin(self, x,y):
        num = str(x*y)
        reverse_num = ''
        for i in range(0,len(num)):
            reverse_num = num[i] + reverse_num
        if(num == reverse_num):
            return True
        else:
            return False
    def largestPalindrome(self, n: int) -> int:
        string = '1'
        r = string.ljust(n + len(string), '0')
        l = string.ljust(n + len(string)-1, '0')
        print(l)
        print(int(r))
        
        for i in reversed(range(int(l),int(r))):
            for j in reversed(range(int(l),int(r))):
                if(self.palin(i,j)):
                    x = i*j
                    return x % 1337
        return 0
