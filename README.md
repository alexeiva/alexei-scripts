### Alexei's scripts for Glyphs App

---

* ### set Kerning Groups for GF Latin Plus.py
This script is derived from @schriftgestalt's [set Kerning Groups][1]
The kerning class declarations have been fully reworked to support [GF Latin Plus][2] and GF Cyrillic Plus Glyphs Sets. 
 
* ### Fix Vertical Metrics
Creates custom parameters in all masters for vertical metrics according to the 125% rule. 

* ### Update WinMetrics
Updates `winAscent` and `winDescent` values. Useful for mastering fonts after adding tall glyphs such as Vietnamese. 
 
#### Acknowlegements
Mark Foley [@m4rc1e][3], Georg Seifert [@schriftgestalt][4]

---
Copyright 2016, Alexei Vanyashin @alexeiva


[1]: https://github.com/schriftgestalt/Glyphs-Scripts/blob/master/Metrics%20%26%20Classes/set%20Kerning%20Groups.py

[2]: https://github.com/google/fonts/tree/master/tools/encodings/GF%202016%20Glyph%20Sets

[3]: https://github.com/m4rc1e/mf-glyphs-scripts

[4]: https://github.com/schriftgestalt/Glyphs-Scripts
