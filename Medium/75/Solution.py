class Solution:
    def sortColors(self, nums: List[int]) -> None:
        arr = []
        count0 = 0
        count1 = 0
        count2 = 0
        
        for num in nums:
            if num == 0:
                count0 += 1
            elif num == 1:
                count1 += 1
            elif num == 2:
                count2 += 1
                
        for i in range(count0):
            arr.append(0)
            
        for i in range(count1):
            arr.append(1)
            
        for i in range(count2):
            arr.append(2)
            
        nums.clear()
        for item in arr:
            nums.append(item)