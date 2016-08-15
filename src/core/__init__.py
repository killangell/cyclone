import sys
import os

cur_dir = os.path.split(os.path.realpath(__file__))[0]
sys.path.insert(0, cur_dir)	

#from lib import *
import lib

__all__ = ['lib']

	
