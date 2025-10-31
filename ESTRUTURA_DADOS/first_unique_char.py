class Solution:
    def firstUniqChar(self, s: str) -> int:
        mydict = {}
        
        for pos, character in enumerate(s):
            if not mydict.get(character):
                mydict[character] = [pos, 1]
            else:
                mydict[character][1] += 1 

        for value in mydict.values():
            if value[1] == 1:
                return value[0]

        return -1


s = "leetcode"
soluction = Solution()


print(soluction.firstUniqChar(s))