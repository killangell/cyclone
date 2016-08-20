#!/bin/sh/python

import core
import unit_test

from core.lib.debug import *
from unit_test.unit_test import UnitTest

SHOW_LEVEL()
INFO("Process start ...\n")
#SET_LEVEL(LEVEL.ERROR)
#SHOW_LEVEL()

ut_obj = UnitTest()
ut_obj.unit_test_entry()





print ""
print ""
input("Enter any key to exit")


