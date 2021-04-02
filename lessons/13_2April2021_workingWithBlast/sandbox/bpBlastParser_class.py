#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Originally written by: Oliver Bonham-Carter
# Ref: BioPython,
# Link: https://biopython.org/docs/dev/api/Bio.Blast.Applications.html#Bio.Blast.Applications.NcbiblastnCommandline

# Comment: A Blast sequence alignment tool using Biopython. Results are parsed by bulit-in parser function.



DATE = "31 Mar 2021"
VERSION = "i"
AUTHOR = "Oliver Bonham-Carter"
AUTHORMAIL = "obonhamcarter@allegheny.edu"



# Bold High Intensity
BIBlack='\033[1;90m'      # Black
BIRed='\033[1;91m'        # Red
BIGreen='\033[1;92m'      # Green
BIYellow='\033[1;93m'     # Yellow
BIBlue='\033[1;94m'       # Blue
BIPurple='\033[1;95m'     # Purple
BICyan='\033[1;96m'       # Cyan
BIWhite='\033[1;97m'      # White

# Regular Colors
Black='\033[0;30m'        # Black
Red='\033[0;31m'          # Red
Green='\033[0;32m'        # Green
Yellow='\033[0;33m'       # Yellow
Blue='\033[0;34m'         # Blue
Purple='\033[0;35m'       # Purple
Cyan='\033[0;36m'         # Cyan
White='\033[0;37m'        # White

# Bold
BBlack='\033[1;30m'       # Black
BRed='\033[1;31m'         # Red
BGreen='\033[1;32m'       # Green
BYellow='\033[1;33m'      # Yellow
BBlue='\033[1;34m'        # Blue
BPurple='\033[1;35m'      # Purple
BCyan='\033[1;36m'        # Cyan
BWhite='\033[1;37m'       # White
BIWhite='\033[1;97m'      # White


def parseResults(myResults):
	""" A function to parse the result of Blast analysis. """
	E_VALUE_THRESH = 1e-20 #upper bound threshold
	for myRecord in NCBIXML.parse(myResults):
		if myRecord.alignments:
			print("\n")
			print(BIYellow + f"query: {myRecord.query[:100]}")
			for align in myRecord.alignments:
				for hsp in align.hsps:
					if hsp.expect < E_VALUE_THRESH:
						print(BICyan + f"match: {align}")
						print(White + f"hsp: {hsp}")


#end of parseResults()

def getVersionNumber():
	"""A function to get the sequence' version number to being an analysis"""
	myPrompt_str = BIGreen + "\tPlease enter the version number : " +White

#TODO

# send this number back to the calling function
	#end of getVersionNumber()


def runBlast(versionNumber_str):
	""" A function to initiate the Blast of sequence. """
	print(BICyan + f"\tCalling Blast analysis for sequence version number : " +BIYellow + f"{versionNumber_str}" +White)


	# TODO


	#Note: nt is nucleotide database, versionNumber_str is the version number of the sequence
	return myResults # send the output of blast back to the calling function
#end of runBlast()

def saveMyResultsToFile(myResults, versionNumber_str):
	"""A function to save results from Blast analysis"""
	# save the output in xml format
	versionNumber_str = versionNumber_str.replace(".","-") # replace any periods in filename with hyphens
	save_file = open(versionNumber_str + ".xml", "w") # save the results as an xml file with extension
	save_file.write(myResults.read())
	save_file.close()
	myResults.close()


def main():
	"""Driver function for the program"""
	print(BIGreen + "\tBlast Analysis.\n\tA version number of a sequence will be required. "+White)

	# ask the user for version number of sequence to analyze by Blast

# TODO

	print("\n")
	print(BIGreen + f"\tParsing results...\n"+White)
# TODO
# end of main()


# import statements
# check that the library is available to the code...
try:
	import Bio
except ModuleNotFoundError:
	print("\t [-]" + BIRed + "\t Error loading BioPython." + White + "\n\t [-]"+BIRed+ "\t Are you using your Docker container?" + White)
	exit()

# from Bio.Seq import Seq # import a sequence library.
from Bio.Blast import NCBIWWW # import the module for BLAST analysis
from Bio.Blast import NCBIXML # import the modeule for the parser

# Run the code by calling main()
main()
