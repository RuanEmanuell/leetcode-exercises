class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_dict = list(dict.fromkeys(nums))
        num_count = [0] * len(num_dict)
        for num in nums:
            pos = num_dict.index(num)
            num_count[pos] += 1
            
        for i in range(len(num_count)):
            if(num_count[i] == 1):
                return num_dict[i]