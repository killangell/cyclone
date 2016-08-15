import core
from core.lib.debug import *

dbg = core.lib.debug.Debug()

import  xml.dom.minidom

class TestCaseXml():  
	def __init__(self, xml_path):  
		self.xml_path = xml_path
		dbg.print_ln(LEVEL.INFO, "TestCaseXml = %s"%(xml_path))
		dom = xml.dom.minidom.parse(xml_path)
		self.root = dom.documentElement

	def show_test_cases(self):
		dbg.print_ln(LEVEL.INFO, "%s" % (self.show_test_cases.__name__))
		pass
	
	def show_object():
		pass

	def show_item():
		pass

