#!/bin/sh/python

from core.lib.debug import *
from unit_test.unit_test_entry import UnitTestEntry

SHOW_LEVEL()
INFO("Process start ...\n")
#SET_LEVEL(LEVEL.ERROR)
#SHOW_LEVEL()

ut_obj = UnitTestEntry()
ut_obj.test_all()





print ""
print ""
input("Enter any key to exit")


