class Solution:
    def hammingWeight(self, n: int) -> int:
        if n in(0,1):
            return n

        restos = 0  
        while n >= 1: 
            restos += n&1
            n >>= 1 

        return restos


n = 11
s = Solution()
print(s.hammingWeight(n))
