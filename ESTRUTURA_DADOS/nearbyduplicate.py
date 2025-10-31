class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        mydict = {}

        for pos, numero in enumerate(nums):
            if not mydict.get(numero):
                mydict[numero] = [pos]
            
            elif (pos - mydict.get(numero)[0]) in list(range(0,k+1,1)):
                return True
                
            else:
                mydict[numero] = [pos]

        return False


soluct = Solution()
nums=[1,2,3,1,2,3]
k = 2

print(soluct.containsNearbyDuplicate(nums,k ))

