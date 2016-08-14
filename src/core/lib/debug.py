class DEBUG_LEVEL(object):
	INFO		= 0
	WARNING		= 1
	ERROR		= 2
	FATAL		= 3

class Debug():  

	def __init__(self, level):  
		self.level = level
		print ("Debug initial level=%d"%(self.level))

	def set_debug_level(self, level):
		self.level = level
		print ("Debug initial level=%d"%(self.level))
		
	def get_debug_level(self):
		return self.level
		
	def print_ln(self, text):
		print(text)
		
if __name__ == '__main__':
	inst = Debug(DEBUG_LEVEL.ERROR)
	inst.print_ln("Debug test output")
	inst.set_debug_level(DEBUG_LEVEL.INFO)
	level = inst.get_debug_level()
	print("level=%d" % level)
	
