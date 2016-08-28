#!/bin/sh/python

from core.lib.debug import *
from unit_test.unit_test_entry import UnitTestEntry

SHOW_LEVEL()
INFO("Process start ...\n")

ut = UnitTestEntry()
ut.test_all()





print ""
print ""
input("Enter any key to exit")


