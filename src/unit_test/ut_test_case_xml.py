import os

from core.public import *
from core.lib.debug import *
from model.test_case_xml import TestCaseXml

class UT_TestCaseXml():  

	def __init__(self):
		cur_path = os.path.split(os.path.realpath(__file__))[0]
		self.xml = TestCaseXml(cur_path + '\ut_test_case.xml')
		self.test_list = []
		self.test_list.append(self.set_up)
		self.test_list.append(self.test_show_test_cases)
		self.test_list.append(self.test_get_path)
		self.test_list.append(self.clean_up)
		
	def set_up(self):
		return TRUE

	def clean_up(self):
		return TRUE
		
	def test_show_test_cases(self):
		INFO("test_show_test_cases")		
		self.xml.show_test_cases()
		
		return TRUE

	def test_get_path(self):
		INFO("test_get_path")
		name_o = "os"
		name_i = "PCIID"
		expect = "os\\vmware\\common\\PCIID"
		real = self.xml.get_path(name_o, name_i)
		assert(expect == real)
		
		name_o = "os"
		name_i = "512E HDD Check"
		expect = "os\\vmware\\common\\512E HDD Check"
		real = self.xml.get_path(name_o, name_i)
		assert(expect == real)

		name_o = "os"
		name_i = "Secure Boot"
		expect = "os\\vmware\\common\\Secure Boot"
		real = self.xml.get_path(name_o, name_i)
		assert(expect == real)
		
		name_o = "os"
		name_i = "LogCheck"
		expect = "os\\vmware\\common\\LogCheck"
		real = self.xml.get_path(name_o, name_i)
		assert(expect == real)

		return TRUE
		
	def test_all(self):
		INFO("test_all len=%d" % len(self.test_list))
		index = 0
		for item in self.test_list:
			index += 1
			INFO("item %d : %s" % (index, item))
			ret = item()
			assert ret == TRUE
		return TRUE

def ut_testcasexml_entry():
	ut = UT_TestCaseXml()
	ut.test_all()
	
	return TRUE
	