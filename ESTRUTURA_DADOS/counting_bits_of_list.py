class Solution:
    
    def countBits(self, n: int) -> list[int]:
        # Monta um range até o valor de n
        # Busca a quantidade de '1' em seu valor binario e addiciona em uma lista
        #ex: range(0,1,2,3) => [0, 1, 1, 2]
        return [self.hammingWeight(i) for i in range(n+1)]


    def hammingWeight(self, n: int) -> int:
        # Retorna A quantidade de '1' em seu valor binario
        if n in(0,1):
            return n
        
        restos = 0
        while n >= 1: 
            restos += n&1
            n = n//2
        return restos


n = 3
s = Solution()
print(s.countBits(n))

n.bit_count()