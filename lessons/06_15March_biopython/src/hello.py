#!/usr/bin/env python3
# -*- coding: utf-8 -*-


DATE = "5 Mar 2021"
VERSION = "i"
AUTHOR = "Oliver Bonham-Carter"
AUTHORMAIL = "obonhamcarter@allegheny.edu"

# Bold colour list
colour_list =['\033[1;30m',
'\033[1;31m',
'\033[1;32m',
'\033[1;33m',
'\033[1;34m',
'\033[1;35m',
'\033[1;36m',
'\033[1;37m',
'\033[1;90m',
'\033[1;91m',
'\033[1;92m',
'\033[1;93m',
'\033[1;94m',
'\033[1;95m',
'\033[1;96m']

BIWhite='\033[1;97m'      # White



banner1_str = """
\t  _  _     _ _
\t | || |___| | |___
\t | __ / -_) | / _ \\
\t |_||_\___|_|_\___/    _ _
\t \ \    / /__ _ _| |__| | |
\t  \ \/\/ / _ \ '_| / _` |_|
\t   \_/\_/\___/_| |_\__,_(_)
   """

# banner ref: https://manytools.org/hacker-tools/ascii-banner/

"""A hello world program.  Cool, right?"""

def get_platformType():
	"""Function to dermine the OS type."""
	platforms = {
	'darwin' : 'OSX',
	'win32'  : 'Windows',
	'linux1' : 'Linux',
	'linux2' : 'Linux'}
	if sys.platform not in platforms:
		return sys.platform
	return platforms[sys.platform]
#end of get_platformType()


def main():
	""" Drives the program"""
	for i in range(3):
		randomColour_str = random.choice(colour_list) # choose a random colour to display the title screen.

	# print the hello world already!!
		print(randomColour_str + banner1_str + BIWhite)

	# report the perceived OS type
	platform_str = get_platformType()

	if platform_str.lower() == "linux" or platform_str.lower() == "osx":
		#print("\t" + " \U0001f5ff \U0001F608 \U0001F601" * 8)
		print("\t This code is running in a Linux or OSX environment.")
		#print("\n\t+ \U0001f600 ")
	else:
		print("\t This code is running in a Windows environment.")
	#end of main()


############################################################################

# import statements
import os, random, sys#, tqdm

# Run the code by calling main()
main()
