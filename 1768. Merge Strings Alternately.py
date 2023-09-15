class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        i = 0

        x = len(word1)
        y = len(word2)


        if(x == y):
            while(i < y):
                ans += word1[i]
                ans += word2[i]
                i += 1


        if(x>y):
            while(i < y):
                ans += word1[i]
                ans += word2[i]
                i += 1
            while(i<x):
                ans += word1[i]
                i += 1
        

        i = 0
        if(x<y):
            while(i < x):
                ans += word1[i]
                ans += word2[i]
                i += 1
            while(i<y):
                ans += word2[i]
                i += 1
            


        return ans
