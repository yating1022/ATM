"""
atm - 

Author: 水果捞
Date: 2024/4/17
Github:https://github.com/yating1022
"""

#ATM程序的执行文件
import os
import sys
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,dir)
print(sys.path)
from ATM.core import main
if __name__ == '__main__':
    main.run()
