#Write a function to finde the longest commmon prefix strin amongst an array of strings.
# If there is no common prefix, return an empty string"".

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        print(strs)
        ans=""
        v = sorted(strs)
        f1 = v[0]
        fl = v[-1]
        for i in range(min(len(f1),len(fl))):
            if(f1[i]!=fl[i]):
                return ans
            ans += f1[i]
            return(ans)
            print(ans)
        # for i in range(len(strs)):
            # print(strs[i])
            # a = list(strs[i])
            # b = []
        
            # print(f"This is v: {v}")





result = Solution()

result.longestCommonPrefix(strs = ["flower", "flow", "flight"])