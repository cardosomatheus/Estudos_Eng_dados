class SolutionSeach:
    def __init__(self):
        pass

    def exponential_search(self,arr, target):
        n = len(arr)-1

        if target > n:
            raise Exception('The target is larger than the array.')

        if arr[0] == target:
            return 0
        
        if arr[n] == target:
            return n

        i = 1
        while i < n and i < target:
            i *= 2
        
        # Menor valor se torna o indice
        i = min(i, n) 
        if arr[i] == target:  return i
        return self.binary_search(arr, target, i//2, i)


    def binary_search(self,nums, n, start_point=0, end_point=0):
        step = 0
        if end_point == 0: 
            end_point  = len(nums)
        
        while start_point < end_point:
            step += 1
            mid = int((start_point+end_point)/2)

            if nums[mid] == n:
                print(f'step: {step}')
                return mid
        
            elif nums[mid] > n:
                end_point = mid

            elif nums[mid] < n:
                start_point = mid





a = [1,2,3]
b = [1,2,3,4,5,6,7,8,9,10]
c = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
d = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42]

search = SolutionSeach()

#print( search.binary_seach(n=32, nums=d))

print(search.exponential_search(arr=d, target=38))
