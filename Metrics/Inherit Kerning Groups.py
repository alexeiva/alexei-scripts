#MenuTitle: Inherit Kerning Groups to suffixed glyphs
# -*- coding: utf-8 -*-
__doc__="""
Inherits Kerning Group to suffixed glyphs (.ssXX) from parent
"""

thisFont = Glyphs.font # frontmost font
thisFontMaster = thisFont.selectedFontMaster # active master
selectedLayers = thisFont.selectedLayers # active layers of selected glyphs

def process( thisLayer ):

	for thisLayer in selectedLayers:
		name = thisLayer.parent.name
		baseName = name
		suffix = None
		periodPos = baseName.find(".")
		if periodPos > 0:
			baseName = name[:periodPos]
			suffix = name[periodPos:]
		baseGlyph = thisFont.glyphs[ baseName ]
		if (baseGlyph.leftKerningGroup != None ):
			thisLayer.parent.leftKerningGroup = ''
			thisLayer.parent.leftKerningGroup = baseGlyph.leftKerningGroup
		if (baseGlyph.rightKerningGroup != None ):
			thisLayer.parent.rightKerningGroup = ''
			thisLayer.parent.rightKerningGroup = baseGlyph.rightKerningGroup
		thisLayer.syncMetrics()

thisFont.disableUpdateInterface() # suppresses UI updates in Font View

for thisLayer in selectedLayers:
	thisGlyph = thisLayer.parent
	print "Processing %s" % thisGlyph.name
	thisGlyph.beginUndo() # begin undo grouping
	process( thisLayer )
	thisGlyph.endUndo()   # end undo grouping

thisFont.enableUpdateInterface() # re-enables UI updates in Font View

# brings macro window to front and clears its log:
Glyphs.clearLog()
Glyphs.showMacroWindow()