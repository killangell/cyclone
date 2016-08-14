import core

dbg_level = 2
dbg = core.lib.debug.Debug(dbg_level)

import  xml.dom.minidom

class TestCaseXml():  
	def __init__(self, xml_path):  
		self.xml_path = xml_path
		dbg.w ("TestCaseXml = %s"%(xml_path))
		dom = xml.dom.minidom.parse(xml_path)
		self.root = dom.documentElement

	def show_test_cases(self):
		dbg.w ("%s" % (self.show_test_cases.__name__))
		pass
	
	def show_object():
		pass

	def show_item():
		pass

