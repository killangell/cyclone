import os

from core.public import *
from core.lib.debug import *
from model.test_case_xml import TestCaseXml

class UT_TestCaseXml():  

	def __init__(self):  
		cur_path = os.path.split(os.path.realpath(__file__))[0]
		self.xml = TestCaseXml(cur_path + '\ut_test_case.xml')
		
	def set_up():
		pass

	def clean_up():
		pass
		
	def test_show_test_cases(self):
		INFO("test_show_test_cases")		
		self.xml.show_test_cases()
		return TRUE

	def test_all(self):
		INFO("test_all")
		assert(TRUE == self.test_show_test_cases())
		
