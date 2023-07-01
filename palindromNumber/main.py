import sys
import os

# Get the current directory of main_script.py
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the 'lib' directory to sys.path
lib_dir = os.path.join(current_dir, '..', 'lib')
sys.path.append(lib_dir)

# Now you can import the module
import logger

logger_instance = logger.setup_logger()

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
