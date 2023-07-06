# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        print("VALID PARENTHESIS")
        a=[]
        for i in range(len(s)):
                       if s[i] == "(" or s[i] == ")":
                               a.append(s[i])
                               print(a)
                               continue
                       else:
                               break
                       print(s[i])
        if a[0] == "(" and a[1] == ")":
                    print("True")
                    return True

result = Solution()

result.isValid(s = "()")