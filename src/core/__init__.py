import sys
import os

cur_dir = os.path.split(os.path.realpath(__file__))[0]
#print(sys.path)
#sys.path.append(cur_dir)	
sys.path.insert(0, cur_dir)	
#print(sys.path)

#from lib import *
import lib

__all__ = ['lib']

d = lib.debug.Debug(3)


if __name__ == '__main__':
	inst = lib.debug.Debug(3)
	inst.print_ln("Class Debug test output")
	
