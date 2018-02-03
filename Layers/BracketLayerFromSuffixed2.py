#MenuTitle: Create Bracket Layer from suffixed child glyph 2
# -*- coding: utf-8 -*-
__doc__="""
Creates a bracket layer from a suffixed(.bold) child glyph. 
Uses weight value of second boldest instance. 2
"""

thisFont = Glyphs.font # frontmost font
thisFontMaster = thisFont.selectedFontMaster # active master
selectedLayers = thisFont.selectedLayers # active layers of selected glyphs

changes = ""
boldWeight = thisFont.instances[-2].weightValue - 1 
boldWeight = str( int( boldWeight )) # convert to int and string from float

for thisLayer in selectedLayers:
	sourceGlyph = thisLayer.parent.name
	name = thisLayer.parent.name
	baseName = name
	suffix = None
	periodPos = baseName.find(".")
	if periodPos > 0:
		baseName = name[:periodPos]
		suffix = name[periodPos:]	
	targetGlyph = baseName	

	newLayer = thisFont.glyphs[ sourceGlyph ].layers[thisFont.masters[-1].id].copy()
	newLayer.associatedMasterId = thisFont.masters[-1].id # attach to last master
	newLayer.name = 'Bold [' + boldWeight + ']'
	newLayer.leftMetricsKey = ''
	newLayer.rightMetricsKey = ''
	thisFont.glyphs [ targetGlyph ].layers.append( newLayer )
	print "Copied %s --> %s in %s" % (sourceGlyph, newLayer.name, targetGlyph)
	changes += "/"+targetGlyph

Glyphs.currentDocument.windowController().addTabWithString_( changes )

