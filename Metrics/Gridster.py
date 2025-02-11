# MenuTitle: Gridster LAT-CYR
# encoding: utf-8
# Copyright: Alexei Vanyashin
# Version: 0.2 for Glyphs3
#
#-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:
# Opens a new tab with Latin and Cyrillic grid tests.
#-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:

import re

# Clear the macro window log for debugging purposes
Glyphs.clearLog()

# Latin and Cyrillic strings
stringLatin = 'abcdefghijklmnopqrstuvwxyz'
stringCyrillic = 'абвгдеёжзийклмнопрстуфхчцшщьъыэюя'

# Initialize outputs
outputLatin = stringLatin + '\n'
outputCyrillic = stringCyrillic + '\n'

# Generate Latin grid (15 lines)
for i in range(15):
    stringLatin = stringLatin[1:] + stringLatin[0]  # Rotate characters
    outputLatin += stringLatin + '\n'

# Add spaces between characters in Latin grid
outputFormattedLatin = re.sub(r'(\S)', r'\1 ', outputLatin)

# Generate Cyrillic grid (15 lines)
for i in range(15):
    stringCyrillic = stringCyrillic[1:] + stringCyrillic[0]  # Rotate characters
    outputCyrillic += stringCyrillic + '\n'

# Add spaces between characters in Cyrillic grid
outputFormattedCyrillic = re.sub(r'(\S)', r'\1 ', outputCyrillic)

# Combine both grids and add an uppercase version
outputFormatted = outputFormattedLatin + outputFormattedCyrillic
outputFormattedUpper = outputFormatted.upper()

# Open new tabs in Glyphs with the generated grids
Font = Glyphs.font
Font.newTab(outputFormatted)
Font.newTab(outputFormattedUpper)