import sys
import os

cur_dir = os.path.split(os.path.realpath(__file__))[0]
print(sys.path)
#sys.path.append(cur_dir)	
sys.path.insert(0, cur_dir)	
print(sys.path)

from debug import *

__all__ = ['debug']


d = Debug(3)

if __name__ == '__main__':
	inst = Debug(3)
	inst.w("Class Debug test output")
