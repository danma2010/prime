#! python

# from: http://cmdlinetips.com/2011/08/three-ways-to-read-a-text-file-line-by-line-in-python/

# Make functions
#def my_split(delimiters, string, maxsplit=0):
#    import re
#    regexPattern = '|'.join(map(re.escape, delimiters))
#    return re.split(regexPattern, string, maxsplit)

import re

print ('Hello, world!')


## Open the file with read only permit
f = open('cat_com.txt')
#f = open(sys.argv[1], "r")

# open a (new) file to write
f_out = open("cat_com.h.txt", "w")

# open a file to append
#outF = open("myOutFile.txt", "a")

delimiters = " ", ";" , ","
regexPattern = '|'.join(map(re.escape, delimiters))
#print(regexPattern)

op_rem = '/'
#op_rem.append['#']
#op_rem.append['a']
#print(op_rem[0])

op_code      = {'SPIWrite': '0x80', 'SPIRead': '0x00', 'WAIT' : '0x30', 'WAIT_CALDONE' : '0x40'}
op_codeIndex = {'SPIWrite': 1   , 'SPIRead': 2   , 'WAIT' : 3   , 'WAIT_CALDONE' : 4}

op_code_waitcaldone = {'TXP': '0x1', 'RXP': '0x2'}


## Read the first line 
lineCnt = 1
commandCnt = 0
line = f.readline()

## If the file is not empty keep reading line one at a time
## till the file is empty


while line:
	# when no debug
	out_line = ''
	# fo debug: with line number
	#out_line = out_line + str(lineCnt) + '> '
	
	# set flags
	lineEnd = 0
	flagOp = 0
	wordIndex = 0
	commandIndex = 0


	# remove lines starting with comment
	if line[0] != op_rem[0]:
		words = re.split(regexPattern, line)
		wordIndex = 0
		
		# go over the words in the line
		for word in words:
			wordIndex = wordIndex + 1
			# remove comments
			if (lineEnd == 1 or word[0] == "/"):
				wordIndex = wordIndex + 1
				lineEnd = 1
			else:
				#print(word)
				# first word: opcode
				if wordIndex == 1 and word in op_code:
					flagOp = 1
					commandCnt = commandCnt + 1
					commandIndex = op_codeIndex[word]
					out_line = out_line+ op_code[word] + ','

				# second word: address / wait / wait_cal-opcode
				if wordIndex == 2:
					if (commandIndex == 1):
						out_line = out_line+ '0x'+str(word) + ','
					if (commandIndex == 2):
						out_line = out_line+ '0x'+str(word) + ','
					if (commandIndex == 3):
						out_line = out_line+ str(word) + ','
					if (commandIndex == 4):
						out_line = out_line+ op_code_waitcaldone[word] + ','

				# third word: data / wait_cal-wait
				if wordIndex == 3:
					if (commandIndex == 1):
						out_line = out_line+ '0x'+str(word) + ','
					#if (commandIndex == 2):
					#	out_line = out_line+ '0x'+str(word) + ','
					#if (commandIndex == 3):
					#	out_line = out_line+ str(word) + ','
					if (commandIndex == 4):
						out_line = out_line+ str(word) + ','
		
		# make the end of line
		if (flagOp == 1):
			out_line = out_line + '              \\' + '\n'
			f_out.write(out_line)
			
	lineCnt = lineCnt + 1
	line = f.readline()
	
f.close()
f_out.close()

print ("Finish Script.")
print (str(lineCnt) + " lines.")
print (str(commandCnt) + " Commands.")
		
		
		

