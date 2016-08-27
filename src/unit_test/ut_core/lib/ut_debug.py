from core.public import *
from core.lib.debug import *

class UT_Debug():  

	def __init__(self):  
		pass
		
	def set_up():
		pass

	def clean_up():
		pass
		
	def test_SET_LEVEL(self):
		INFO("test_SET_LEVEL")
		
		SHOW_LEVEL()
		old_level = GET_LEVEL()
				
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
		INFO("test_all")
		self.test_SET_LEVEL()

		return TRUE
		

