import sys
import os

lib_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'lib')
sys.path.append(lib_dir)

from my_logger import setup_logger

logger_instance = setup_logger()

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        logger_instance.info('Class Called.')
        print(f"nums: {nums}")
        print(f"val: {val}")
        i = len(nums) - 1
        while i >= 0:
            if nums[i] == val:
                nums.remove(nums[i])
            i -= 1
        k = nums
        print(f"k: {k}")
        print(len(k))
        return len(k)

result = Solution()
result.removeElement(nums=[3,2,2,3], val=3)