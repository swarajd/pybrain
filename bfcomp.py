arr = [0]
index = 0

def runCode(prgm):
	global arr
	global index
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
			if len(arr) - 1 < index + 1:
				arr.append(0)
				index += 1
			else:
				index += 1
			#print(index)
		elif prgm[i] == '<':
			if index == 0:
				index = 0
			else:
				index -= 1
			#print(index)
		elif prgm[i] == '+':
			arr[index] += 1
			#print(index,arr[index])
		elif prgm[i] == '-':
			arr[index] -= 1
			#print(index,arr[index])
		elif prgm[i] == '.':
			print(chr(arr[index]))
		elif prgm[i] == ',':
			ch = input()
			arr[index] = ord(ch[0])
		elif prgm[i] == '[':
			starts.append(i)
		elif prgm[i] == ']':
			#print('is this parsed?')
			if len(starts) != 0:
				ends.append(i)
				start = starts.pop()
				end = i
				loops[start] = end
				loops[end] = start
			if ((i in loops.values()) and (i > loops[i]) and arr[index] > 0):
				i = loops[i]
				#print("this is parsed",i)
		else:
			pass
		i += 1
	#print(loops)
			
runCode(">+++++++++[<++++++++>-]<.>+++++++[<++++>-]<+.+++++++..+++.[-]>++++++++[<++++>-] <.>+++++++++++[<++++++++>-]<-.--------.+++.------.--------.[-]>++++++++[<++++>- ]<+.[-]++++++++++.")

