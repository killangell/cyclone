#!/bin/sh/python

import core
import unit_test

dbg = core.lib.debug.Debug(2)

unit_test_obj = unit_test.unit_test.UnitTest()
unit_test_obj.run_test()


