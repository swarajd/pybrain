from ByteArray import byteArray

def runCode(prgm):
	b = byteArray()
	lnum = 0
	rnum = 0
	starts = []
	ends = []
	loops = {}
	for i in prgm:
		if i not in ['+','-','.','>','<','[',']',' ']:
			print("this doesn't compile")
			return
		if i == '[':
			lnum += 1
		elif i == ']':
			rnum += 1
	if lnum != rnum:
		print("this doesn't compile")
		return
	i = 0
	while i < len(prgm):
		if prgm[i] == '>':
			if b.pos >= 29999:
				continue
			else:
				b.advance()
		elif prgm[i] == '<':
			if b.pos <= 0:
				b.pos = 0
			else:
				b.devance()
		elif prgm[i] == '+':
			b.increment()
		elif prgm[i] == '-':
			b.decrement()
		elif prgm[i] == '.':
			print(chr(b.get()))
		elif prgm[i] == ',':
			ch = input()
			b.set(ch[0])
		elif prgm[i] == '[':
			starts.append(i)
		elif prgm[i] == ']':
			if len(starts) != 0:
				ends.append(i)
				start = starts.pop()
				end = i
				loops[start] = end
				loops[end] = start
			if ((i in loops.values()) and (i > loops[i]) and b.get() > 0):
				i = loops[i]
		else:
			pass
		i += 1
			
runCode(">+++++++++[<++++++++>-]<.>+++++++[<++++>-]<+.+++++++..+++.[-]>++++++++[<++++>-] <.>+++++++++++[<++++++++>-]<-.--------.+++.------.--------.[-]>++++++++[<++++>- ]<+.[-]++++++++++.")

