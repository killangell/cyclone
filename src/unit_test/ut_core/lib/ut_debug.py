from core.public import *
from core.lib.debug import *

class UT_Debug():  

	def __init__(self):  
		self.old_level = LEVEL.INFO
		self.test_list = []
		self.test_list.append(self.set_up)
		self.test_list.append(self.test_SET_LEVEL)
		self.test_list.append(self.clean_up)
		
	def set_up(self):
		self.old_level = GET_LEVEL()
		return TRUE

	def clean_up(self):
		SET_LEVEL(self.old_level)
		return TRUE
		
	def test_SET_LEVEL(self):
		INFO("test_SET_LEVEL")
		
		SET_LEVEL(LEVEL.INFO)
		INFO("Show on Info level.")
		WARNING("Show on WARNING level.")
		ERROR("Show on ERROR level.")
		FATAL("Show on FATAL level.")
		
		SET_LEVEL(LEVEL.WARNING)
		INFO("INFO, If some problem, you'll see me.")
		WARNING("Show on WARNING level.")
		ERROR("Show on ERROR level.")
		FATAL("Show on FATAL level.")		

		SET_LEVEL(LEVEL.ERROR)
		INFO("INFO, If some problem, you'll see me.")
		WARNING("WARNING, If some problem, you'll see me.")
		ERROR("Show on ERROR level.")
		FATAL("Show on FATAL level.")
		
		SET_LEVEL(LEVEL.FATAL)
		INFO("INFO, If some problem, you'll see me.")
		WARNING("WARNING, If some problem, you'll see me.")
		ERROR("ERROR, If some problem, you'll see me.")
		FATAL("Show on FATAL level.")
		
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
		
def ut_debug_entry():
	ut = UT_Debug()
	ut.test_all()

	return TRUE
	
