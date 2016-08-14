import core
import model
import os

dbg_level = 2
dbg = core.lib.debug.Debug(dbg_level)

class UT_TestCaseXml():  

	def __init__(self):  
		cur_path = os.path.split(os.path.realpath(__file__))[0]
		self.xml = model.test_case_xml.TestCaseXml (cur_path + '\ut_test_case.xml')

	def set_up():
		pass

	def clean_up():
		pass
		
	def test_show_test_cases(self):
		ret = 0
		dbg.print_ln ("%s" % (self.test_show_test_cases.__name__))
		self.xml.show_test_cases()
		return ret
		
