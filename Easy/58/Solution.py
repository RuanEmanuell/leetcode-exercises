class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        parts = s.split()
        return len(parts[len(parts) - 1])
        