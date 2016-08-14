class Debug():  
	def __init__(self, level):  
		self.level = level
		print ("Debug initial level=%d"%(level))
	def w(self, text):
		print(text)
		
if __name__ == '__main__':
	inst = Debug(3)
	inst.w("Debug test output")
	
