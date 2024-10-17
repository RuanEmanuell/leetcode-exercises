import string
import re

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        alphabet = string.ascii_lowercase
        
        dot_count = 0 
        colon_count = 0 
        
        if len(queryIP) > 0 and len(queryIP) <= 15 and queryIP[0] != '0' and queryIP[0].isnumeric() == True and queryIP[len(queryIP) - 1].isnumeric() == True and ":" not in queryIP and re.search('[a-zA-Z]', queryIP) == None:
            for i in range(len(queryIP)):
                if queryIP[i] == "." or i == 0:
                    if i < len(queryIP) - 3:
                        isnt_dot = 0
                        if(i == 0):
                            isnt_dot += 1
                        for j in range(i+1, i+4):
                            if queryIP[j] != ".":
                                isnt_dot += 1
                            else:
                                isnt_dot = 0
                        if isnt_dot > 3:
                            return "Neither"
                    if i > 0:
                        if i < len(queryIP) - 1 and (queryIP[i+1] == '0' or queryIP[i+1].isnumeric() == False):
                                if queryIP[i+2] != ".":
                                    print(queryIP[i+2])
                                    return "Neither"
                        if i < len(queryIP) - 3 and (int(queryIP[i+1]) >= 2 and int(queryIP[i+2]) >= 5 and int(queryIP[i+3]) >= 6):
                                return "Neither"
                    if queryIP[i] == ".":
                        dot_count += 1
                else:
                    if queryIP[i].isnumeric() == False:
                        return "Neither"
                
        if dot_count == 3:
            return "IPv4"
        
        if len(queryIP) > 0 and len(queryIP) <= 39 and (queryIP[len(queryIP) - 1].isnumeric() == True or queryIP[len(queryIP) - 1].lower() in alphabet):
            for i in range(len(queryIP)):
                if queryIP[i] == ":":
                    if i + 6 <= len(queryIP):
                        isnt_colon = 0
                        for j in range(i, i+6):
                            if queryIP[j] != ":":
                                isnt_colon += 1
                        if isnt_colon == 5:
                            return "Neither"
                    if i+1 < len(queryIP) and queryIP[i+1].isnumeric() == False and queryIP[i+1].lower() not in alphabet:
                            return "Neither"
                    colon_count += 1
                else:
                    if queryIP[i].isnumeric() == False and queryIP[i].lower() in alphabet:
                        if alphabet.index(queryIP[i].lower()) >= 6:
                            return "Neither"
                            
        
        if colon_count == 7:
            return "IPv6"
            
        return "Neither"