class LEVEL(object):
	INFO		= 0
	WARNING		= 1
	ERROR		= 2
	FATAL		= 3

class Debug():  
	
	def __init__(self):  
		self.level = LEVEL.INFO
		print ("Debug initial level=%d"%(self.level))

	def set_debug_level(self, level):
		self.level = level
		print ("Debug initial level=%d"%(self.level))
		
	def get_debug_level(self):
		return self.level
		
	def print_ln(self, level, text):
		if level >= self.level:
			print(text)
		
if __name__ == '__main__':
	inst = Debug()
	inst.print_ln(LEVEL.INFO, "Debug test output")
	inst.set_debug_level(LEVEL.INFO)
	level = inst.get_debug_level()
	print("level=%d" % level)
	
