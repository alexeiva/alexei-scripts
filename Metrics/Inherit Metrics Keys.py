#MenuTitle: Inherit Metrics Keys to suffixed glyphs
# -*- coding: utf-8 -*-
__doc__="""
Inherits Metrics Keys to suffixed glyphs (.ssXX) from parent
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
		thisLayer.leftMetricsKey = baseName
		thisLayer.rightMetricsKey = baseName
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