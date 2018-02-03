#MenuTitle: Gridster LAT-CYR
# encoding: utf-8
# Copyright: Alexei Vanyashin, 2017, Version 0.1
#
#-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:
# Opens a new tab with Latin and Cyrillic grid tests.
#-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:

import re
Glyphs.clearLog() # clears macro window log

stringLatin = 'abcdefghijklmnopqrstuvwxyz'
outputLatin = stringLatin + '\n'

string = 'абвгдеёжзийклмнопрстуфхчцшщьъыэюя'
string = string.decode('utf-8')
output = string + '\n' # adding line breaks to string

for i in range(15):	# prints x lines of Latin grid test
	stringLatin = re.sub('^(\S){1}(.*)', r"\2\1", stringLatin)
	outputLatin += stringLatin + '\n'

outputFormatted = re.sub('(\S{1})', r"\1 ", outputLatin) # adding spaces

for i in range(15):	# prints x lines of Cyrillic grid test
	string = re.sub('^(\S){1}(.*)', r"\2\1", string)
	output += string + '\n'

outputFormatted += re.sub('(\S{1})', r"\1 ", output) # adding spaces
outputFormattedUpper = outputFormatted.upper()

Glyphs.currentDocument.windowController().addTabWithString_( outputFormatted )
Glyphs.currentDocument.windowController().addTabWithString_( outputFormattedUpper )
