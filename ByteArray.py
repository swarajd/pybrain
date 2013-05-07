class byteArray:
	def __init__(self):
		self.grid = [0] * 30000
		self.pos = 0
	def advance(self):
		self.pos += 1
	def devance(self):
		self.pos -= 1
	def increment(self):
		self.grid[self.pos] += 1
	def decrement(self):
		self.grid[self.pos] -= 1
	def jump(self,index):
		self.pos = index
	def set(self,ch):
		self.grid[self.pos] = ord(ch)
	def get(self):
		return self.grid[self.pos]
	def getVal(self,index):
		return self.grid[index]
		
		

