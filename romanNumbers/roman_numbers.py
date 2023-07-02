class Solution:
    def romanToInt(self, s:str) -> int:
        print(s)
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        ans = 0
        n=0
        print(m)
        for i in range(len(s)):
            print(m[s[i]])

result = Solution()

result.romanToInt(s="MCMXCIV")