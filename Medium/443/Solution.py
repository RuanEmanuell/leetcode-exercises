class Solution:
    def compress(self, chars: List[str]) -> int:
        arr = []
        
        current_count = 0
        current_char = ""
        for i in range(len(chars)):
            if i == 0:
                current_char = chars[i]
                current_count += 1
            elif current_char != chars[i]:
                arr.append(current_char)
                if current_count > 1:
                    arr.extend(list(str(current_count)))
                current_char = chars[i]
                current_count = 1
            else:
                current_count += 1

            if i == len(chars) - 1:  
                arr.append(current_char)
                if current_count > 1:
                    arr.extend(list(str(current_count)))
                    
        chars[:] = arr
        return len(chars)