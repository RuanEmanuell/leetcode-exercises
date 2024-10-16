class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numberDict = list(dict.fromkeys(numbers))
        for i in range(len(numbers)):
                for j in range(len(numberDict)):
                    if numbers[i] + numberDict[j] == target and i != j:
                            if(i+1 == len(numbers) - numbers[-1::-1].index(numberDict[j])):
                                return [i, len(numbers) - numbers[-1::-1].index(numberDict[j])]
                            else:
                                return [i+1, len(numbers) - numbers[-1::-1].index(numberDict[j])]