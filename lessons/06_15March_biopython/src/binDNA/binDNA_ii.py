#!/usr/bin/env python3
# -*- coding: utf-8 -*-


DATE = "11 Mar 2021"
VERSION = "ii"
AUTHOR = "Oliver Bonham-Carter"
AUTHORMAIL = "obonhamcarter@allegheny.edu"

BIGreen='\033[1;92m'      # Green
Yellow='\033[0;33m'       # Yellow
BIYellow='\033[1;93m'     # Yellow
BIWhite='\033[1;97m'      # Bright White
White='\033[0;37m'        # White

# conversion dictionaries
dnaCode_dic = {"a": "00", "c": "01", "t": "11", "g": "10"}
binCode_dic = {"00":"a", "01":"c", "11":"t", "10":"g"}

def help():
	print("""
		Date: 11 March 2021
		Program to convert binary into DNA
		and DNA into binary, depending on
		input options.

		(For text file of binary information
		to be converted into DNA)
			[+] Usage: binDNA.py bin.txt dna

		(For text file of DNA information
		to be converted into binary)
			[+] Usage: binDNA.py dna.txt bin
		""")
	print("\t [+] The conversion dictionaries are the following")
	print("\t DNA to binary conversions :",dnaCode_dic)
	print("\t Binary to DNA conversions :",binCode_dic)
# end of help()



def openFile(inFile):

	try:
		data_str = open(inFile,"r").readline()
		data_str = data_str.replace("\n","")
		return data_str
	except IOError:
		print(" Bad file name. Quitting")
		exit()
#end of openFile()


def makeDNA(in_str):
# method to convert bin into dna
# input: 1010111
# output: atacga

	tmp_str = ""

	print("\n\t[+] Input string :" + BIGreen +f"{in_str}"+White)

	if len(in_str) % 2 != 0:
		in_str = in_str + "0"

	for i in range(0, len(in_str), 2):
#        print i, in_str[i:i+2]
		tmp_str = tmp_str + binCode_dic[in_str[i:i+2]]
	return tmp_str

#end of makeDNA()


def makeBinary(in_str):
# method to convert dna into bin
# input: atagatac
# output: 1010101
	tmp_str = ""

	print("\n\t[+] Input string :" + BIGreen +f"{in_str}"+White)

	for i in in_str:
		tmp_str = tmp_str + dnaCode_dic[i]
	return tmp_str

#end of makeBinary()



def begin(inFile_str,task_str):
	# main method of the program. Called by the command-line arguments
	#data_str = string.lower(openFile(inFile_str))
	data_str = (openFile(inFile_str)).lower()
	#task_str = string.lower(task_str)
	task_str = task_str.lower()
	output_str = "none"
#    print "\n  Input string is the following :",data_str

	if task_str == "bin": #we are making a binary sequence from dna
		print("\t[+] Preparing a binary sequence from DNA")
		print("\t","_" * 20)
		output_str = makeBinary(data_str)

	if task_str == "dna" : # make a dna sequence from binary
		print("\t[+] Preparing a DNA sequence from binary")
		print("\t","_" * 20)
		output_str = makeDNA(data_str)

	print("\t[+] Output sequence :"+Yellow+f"{output_str}\n"+White)
#end of begin()


import string,sys
if __name__ == '__main__':
#       if len(sys.argv) == 2: #one option added to command line
#       begin(sys.argv[1])

	if len(sys.argv) == 3:
		begin(sys.argv[1],sys.argv[2])
	else:
		help()
		sys.exit(0)
