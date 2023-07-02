import sys
import os

lib_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'lib')
sys.path.append(lib_dir)

from my_logger import setup_logger

logger_instance = setup_logger()

class Palindrome:
    def __init__(self):
        self.name = "Palindrome"
        logger_instance.info('Class Called.')

    def isPalindrome1(self, x: int) -> bool:
        logger_instance.info('Function Called.')
        logger_instance.info(f'Is {x} a Palindrome?')
        x = str(x)
        r = list(x[::-1])
        while True:    
            for i in range(len(x)):
                if x[i] != r[i]:
                    return False
            return True

result = Palindrome()

print(result.isPalindrome1(x=121))
