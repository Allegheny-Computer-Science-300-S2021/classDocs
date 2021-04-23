#!/usr/bin/env python3
# -*- coding: utf-8 -*-


DATE = "22 April 2021"
VERSION = "i"
AUTHOR = "Oliver Bonham-Carter"
AUTHORMAIL = "obonhamcarter@allegheny.edu"

threshold = 100 # the maximum length of proteins to be reported.


# colour codes

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


# define the codon table for translation.
DNACodonTable_dict = {
	'TTT': 'F',     'CTT': 'L',     'ATT': 'I',     'GTT': 'V',
	'TTC': 'F',     'CTC': 'L',     'ATC': 'I',     'GTC': 'V',
	'TTA': 'L',     'CTA': 'L',     'ATA': 'I',     'GTA': 'V',
	'TTG': 'L',     'CTG': 'L',     'ATG': 'M',     'GTG': 'V',
	'TCT': 'S',     'CCT': 'P',     'ACT': 'T',     'GCT': 'A',
	'TCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
	'TCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
	'TCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
	'TAT': 'Y',     'CAT': 'H',     'AAT': 'N',     'GAT': 'D',
	'TAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
	'TAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
	'TAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
	'TGT': 'C',     'CGT': 'R',     'AGT': 'S',     'GGT': 'G',
	'TGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
	'TGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
	'TGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}




def helper():

	"""Cheap online help; how to use the program"""
	h_str1 = "\t"+ BIBlue + DATE+" | version: "+VERSION + White
	h_str2 = "\t"+ BIBlue + AUTHOR +"\n\tmail: "+AUTHORMAIL + White
	print("\t"+len(h_str2) * "-")
	print(h_str1)
	print("\t"+len(h_str2) * "-")
	print(h_str2)
	print("\t"+len(h_str2) * "-")
	print(White + """
Open Reading Frames
===================

Either strand of a DNA double helix can serve as the coding strand for RNA
transcription. Hence, a given DNA string implies six total reading frames, or
ways in which the same region of DNA can be translated into amino acids: three
reading frames result from reading the string itself, whereas three more
result from reading its reverse complement.

An open reading frame (ORF) is one which starts from the start codon and ends
by stop codon, without any other stop codons in between. Thus, a candidate
protein string is derived by translating an open reading frame into amino
acids until a stop codon is reached.

Given: A DNA string s of length at most 1 kbp.

Return: Every distinct candidate protein string that can be translated from
ORFs of s. Strings can be returned in any order.

Sample Dataset
--------------
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG

Sample Output
-------------
MLLGSFRLIPKETLIQVAGSSPCNLS
M
MGMTPRLGLESLLE
MTPRLGLESLLE
""")
	print(BICyan + "\tUses python3")
	print(BIGreen + "\t [+] To run:" + BIYellow + "\n\t python3 orf_finder.py fleckOrchid_fasta.txt"+White)
	print(BIGreen + "\t [+] Or:" + BIYellow + "\n\t python orf_finder.py fleckOrchid_fasta.txt"+White)

	#end of helper()


def translate_codon(codon):
	""" Translate the DNA to protein. Note we could also have used BioPython for this task. Note the extra code we had to include in this source."""
	protein = None
	if len(codon) == 3 and codon in DNACodonTable_dict:
		protein = DNACodonTable_dict[codon]
	return protein


def reverse_complement(dna):
	lookup_dict = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
	return ''.join([lookup_dict[c] for c in reversed(dna)]) # convert to complement seq


def possible_protein_strings(s):
	""" A function to return potential ORFs by reading in DNA, translating sequence to protein and then checking for START and STOP codons. """
	results = []
	indices = []

	l = len(s)
	for i in range(l):
		protein = translate_codon(s[i:i+3])
		if protein and protein == 'M':
			indices.append(i)

	for i in indices:
		found_stop = False
		protein_string = ''

		for j in range(i, l, 3):
			protein = translate_codon(s[j:j+3])

			if not protein:
				break

			if protein == 'Stop':
				found_stop = True
				break

			protein_string += protein

		if found_stop:
			results.append(protein_string)

	return results


def printer(output):
	""" A function to printout the results according to seq length"""
	# print("  Output :", output, type(output))
	print(BIGreen + "\n\t ________  Detected (Potential) ORFs ________\n" + White)
	#output_list = string.split(output)
	output_list = output.split()
	counter = 0
	for i in output_list:
		if len(i) <= threshold:
			print("\t" + BIGreen + str(counter) + BIYellow + f"\t {i}" + White)
			counter += 1

#end of printer()


def getSeq(myFile_str):
	""" A function to load text file and format the sequence"""
	mySeq_str = open(myFile_str).read().strip()
	return mySeq_str # send the sequence back to the calling function
#end of geteq()

def getFastaSeq(myFile_str):
	"""A function to use Biopython to load a FASTA file and return the seq"""
	print(BICyan + "\n\t Loading FASTA file ..." + White)
	from Bio import SeqIO
	seq = ""
	with open(myFile_str) as handle:
		for record in SeqIO.parse(handle, "fasta"):
			print(BIGreen + "\t [+] Record    :" + BIYellow + f" {record.id}")
			seq = record.seq # pull out the sequence
	return seq
	#end of getFastaSeq()



def main(myFile_str):
	"""Main driver of the program"""

	# myData_str = getSeq(myFile_str) # loads a text file containing only sequence
	myData_str = getFastaSeq(myFile_str) # loads a FASTA file, returns sequence
	print(BIGreen + "\t [+] Sequence  :" + BIYellow + f" {myData_str}")
	print(BIGreen + "\t [+] Threshold :" + BIYellow + f" {threshold}")

	possible_a = possible_protein_strings(myData_str)
	possible_b = possible_protein_strings(reverse_complement(myData_str))

	output = "\n".join(set(possible_a + possible_b))
	printer(output)

	# end of main()


# # command line paramters code
# ###################################
import sys
if __name__ == '__main__':

 # First check that the BioPython library is available to the code ...
	try:
		import Bio
	except ModuleNotFoundError:
		print("\t [-]" + BIRed + "\t Error loading BioPython." + White + "\n\t [-]"+BIRed+ "\t Are you using your Docker container?" + White)
		exit()


# Then run the code ...

	if len(sys.argv) == 2: #one option added to command line
		main(sys.argv[1])
	else:
		helper() # display help if no file entered
		sys.exit(0)
