class Solution:    
    
    def romanToInt(self, s: str) -> int:
        m = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        }
        r=0
        i=0
        while i < len(s):
            j = i+1
            k=1
            while j < len(s) and s[j]==s[i]:
                k+=1
                j+=1
            q = m[s[j-1]]*k             
            if j<len(s) and m[s[i]]<m[s[j]]:
                q=-q
            i = j
            r+=q
        return r
