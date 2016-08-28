from core.lib.debug import *
import xml.dom.minidom

class Item():

	def __init__(self):
		self.name = "undefined"
		self.path = "undefined"
		
	def set_name(self, name):
		self.name = name
		
	def get_name(self):
		return self.name

	def set_path(self, path):
		self.path = path
		
	def get_path(self):
		return self.path

class Object():

	def __init__(self):
		self.name = "undefined"
		self.items = {}
		
	def set_name(self, name):
		self.name = name
		
	def get_name(self):
		return self.name

	def set_items(self, items):
		self.items = items
		
	def get_items(self):
		return self.items

class TestCase():

	def __init__(self):
		self.objects = {}
		
	def set_objects(self, objects):
		self.objects = objects
		
	def get_objects(self):
		return self.objects

class TestCaseXml():  

	def __init__(self, xml_path):
		INFO("TestCaseXml is %s" %(xml_path))
		self.tc = self.parse(xml_path)
		
	def parse(self, xml_path):
		INFO("parse")
		tc = TestCase()
		dom = xml.dom.minidom.parse(xml_path)
		root = dom.getElementsByTagName("testcase")[0]
		objects = root.getElementsByTagName("object")
		for object in objects:
			name = object.getElementsByTagName("name")[0].childNodes[0].nodeValue

			o = Object()
			o.set_name(name)
			tc.get_objects()[name] = o
			
			items = object.getElementsByTagName("items")[0]
			subitems = items.getElementsByTagName("item")
			for item in subitems:
				name = item.getElementsByTagName("name")[0].childNodes[0].nodeValue
				path = item.getElementsByTagName("path")[0].childNodes[0].nodeValue

				i = Item()
				i.set_name(name)
				i.set_path(path)
				o.get_items()[name] = i
				
		return tc

	def show_test_cases(self):
		INFO("show_test_cases")
		objects = self.tc.get_objects()
		
		for n,object in objects.items():
			INFO("o : " + n)
			i = object.get_items()
			
			for n,item in i.items():
				INFO("  n : " + item.get_name())
				INFO("  p : " + item.get_path())

	def get_path(self, name_o, name_i):
		objects = self.tc.get_objects()
		items = objects[name_o].get_items()
		item = items[name_i]
		path = item.get_path()

		return path

