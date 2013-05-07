class byteArray:
	def __init__(self):
		self.grid = [0] * 30000
		self.pos = 0
	def advance(self):
		self.pos += 1
	def reverse(self):
		self.pos -= 1
	def add(self):
		self.grid[self.pos] += 1
	def subtract(self):
		self.grid[self.pos] -= 1
	def jump(self,index):
		self.pos = index
	def getVal(self,index):
		return self.grid[index]
		
		

