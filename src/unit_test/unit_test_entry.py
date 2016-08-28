from core.public import *
from core.lib.debug import *
from ut_test_case_xml import ut_testcasexml_entry
from unit_test.ut_core.lib.ut_debug import ut_debug_entry
	
class UnitTestEntry():

	def __init__(self):
		self.test_list = []
		self.test_list.append(ut_debug_entry)
		self.test_list.append(ut_testcasexml_entry)
		
	def test_all(self):
		INFO("test_all len=%d" % len(self.test_list))
		index = 0
		for item in self.test_list:
			index += 1
			INFO("item %d : %s" % (index, item))
			ret = item()
			assert ret == TRUE
		return TRUE
		