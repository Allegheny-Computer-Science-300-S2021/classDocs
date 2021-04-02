from Bio.Blast import NCBIXML
print("\tA parser for a xml file from a Blast analysis.")
fileName_str = input("\t Enter filename of results file : ")

#fileName_str = ""
E_VALUE_THRESH = 1e-20
for myRecord in NCBIXML.parse(open(fileName_str)):
	if myRecord.alignments:
		print("\n")
		print("query: %s" % myRecord.query[:100])
		for align in myRecord.alignments:
			for hsp in align.hsps:
				if hsp.expect < E_VALUE_THRESH:
#					print("match: %s " % align.title[:100])
#					print("match: %s " % align)
					print(f"match: {align}")
					print(f"hsp: {hsp}")
