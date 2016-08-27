class LEVEL(object):
	INFO		= 0
	WARNING		= 1
	ERROR		= 2
	FATAL		= 3

class Debug():  
	
	def __init__(self):  
		self.level = LEVEL.INFO

	def set_debug_level(self, level):
		self.level = level
		print ("Debug initial level=%d"%(self.level))
		
	def get_debug_level(self):
		return self.level
		
	def print_ln(self, level, text):
		if level >= self.level:
			print(text)

g_dbg = Debug()

def INFO(text):
	g_dbg.print_ln(LEVEL.INFO, text)
	

def WARNING(text):
	g_dbg.print_ln(LEVEL.WARNING, text)
	
def ERROR(text):
	g_dbg.print_ln(LEVEL.ERROR, text)
	
def FATAL(text):
	g_dbg.print_ln(LEVEL.FATAL, text)
	
def SET_LEVEL(level):
	g_dbg.set_debug_level(level)	
	
def GET_LEVEL():
	return g_dbg.get_debug_level()
	
def SHOW_LEVEL():
	level = GET_LEVEL()
	print ("Current level=%d"%(level))
	
if __name__ == '__main__':
	inst = Debug()
	inst.print_ln(LEVEL.INFO, "Debug test output")
	inst.set_debug_level(LEVEL.INFO)
	level = inst.get_debug_level()
	print("level=%d" % level)
	
