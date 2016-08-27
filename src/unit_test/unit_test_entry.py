'''
import sys
import os
print sys.path
'''

from core.public import *
from core.lib.debug import *
from ut_test_case_xml import UT_TestCaseXml
from unit_test.ut_core.lib.ut_debug import UT_Debug

def test_ut_test_case_xml():
	ut_obj = UT_TestCaseXml()
	return ut_obj.test_all()
	
def test_ut_debug():
	ut_obj = UT_Debug()
	return ut_obj.test_all()
	

class UnitTestEntry():

	def __init__(self):  
		pass
		
	def test_all(self):
		INFO("test_all")
		ret = test_ut_test_case_xml()
		assert ret == TRUE
		ret = test_ut_debug()
		assert ret == TRUE
		

