from core.lib.debug import *
from ut_test_case_xml import UT_TestCaseXml

def test_ut_test_case_xml():
	ut_obj = UT_TestCaseXml()
	return ut_obj.test_show_test_cases()

class UnitTest():  

	def __init__(self):  
		pass
		
	def unit_test_entry(self):
		INFO("unit_test_entry")
		ret = test_ut_test_case_xml()
		assert ret == 0
		

