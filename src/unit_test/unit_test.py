import core
import ut_test_case_xml

dbg = core.lib.debug.Debug(2)

def test_ut_test_case_xml():
	ut_test_case_xml_obj = ut_test_case_xml.UT_TestCaseXml()
	return ut_test_case_xml_obj.test_show_test_cases()

class UnitTest():  

	def __init__(self):  
		pass
		
	def unit_test_entry(self):
		ret = test_ut_test_case_xml()
		assert ret == 0
		

