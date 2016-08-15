import sys
import os

cur_dir = os.path.split(os.path.realpath(__file__))[0]
sys.path.insert(0, cur_dir)	

import debug
#from debug import *

__all__ = ['debug']

