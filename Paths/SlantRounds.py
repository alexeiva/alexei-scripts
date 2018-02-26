#MenuTitle: Slant Rounds
# -*- coding: utf-8 -*-
# The slanting algorithm is based on the
# method by Jacques Le Bailly <fonthausen@baronvonfonthausen.com>
# Copyright 2017 Alexei Vanyashin <a@cyreal.org>
__doc__="""
Slants round glyphs with vertical compensation. Based on method by Jacques Le Bailly
"""

import GlyphsApp

thisFont = Glyphs.font # frontmost font
selectedLayers = thisFont.selectedLayers # active layers of selected glyphs

def process( thisLayer ):
	thisMasterAngle = thisLayer.associatedFontMaster().italicAngle
	myY = thisMasterAngle / 100 
	myX = -thisMasterAngle / 100 
	
	thisLayer.beginChanges()
		
	# shear:
	oldPos = thisLayer.bounds.origin
	thisLayer.applyTransform([1, myX, myY*2, 1, 0, 0])
	thisLayer.addNodesAtExtremes()
	
	# move back:
	newPos = thisLayer.bounds.origin
	xShiftBack = oldPos.x-newPos.x
	yShiftBack = oldPos.y-newPos.y
	thisLayer.applyTransform([1, 0, 0, 1, xShiftBack, yShiftBack])
	
	thisLayer.endChanges()
	
	print "y-shift: %s, x-shift: %s" % (abs(yShift[2]), xShift[2])


thisFont.disableUpdateInterface() # suppresses UI updates in Font View
print "*** Start Rounding Glyphs\n"

try: 
	for thisLayer in selectedLayers:
		if not (thisLayer.glyphMetrics()[5] > 0):
			print "Italic Angle should be greater than zero. Set Italic Angle in Font Master"
			break
		print "Rounding glyph '%s' -> " % (thisLayer.parent.name),
		process( thisLayer )
		thisLayer.syncMetrics()

	for thisLayer in selectedLayers[:-1]: # Last layer
  		print "Done. Clean up nodes if necessary."
except TypeError: 
	print "No glyphs selected. Select glyphs and rerun script."
print "\n***"

thisFont.enableUpdateInterface() # re-enables UI updates in Font View
