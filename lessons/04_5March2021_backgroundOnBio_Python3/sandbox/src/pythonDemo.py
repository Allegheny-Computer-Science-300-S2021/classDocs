
print("Welcome to the program!")
prmpt_str = " Please enter your name :"

# place the string above into input statement
name_str = input(prmpt_str)
print(" Your name is :",name_str)
print(" And is <<",len(name_str),">> chars long!")

# print the chars on lines
print(" What are the characters in the string? ")

for i in range(len(name_str)):
	# note the tabs for this block!
	# we iterate through the positions in string
	print("  + char :",name_str[i])

# findout how many a's are in the name
numChar_int = name_str.count("a")
print(" The number of a's in your name :",numChar_int)
