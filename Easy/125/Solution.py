import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'\W+', '', s)
        s = s.replace('_', '')
        s = s.strip().lower()
        return s == s [::-1]