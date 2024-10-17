class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = str(bin(n)[2:])
        num = 0
        
        for bit in binary:
            if bit == '1':
                num += 1
        return num