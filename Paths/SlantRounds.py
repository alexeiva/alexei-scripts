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

yShift = []
xShift = []
def process( thisLayer ):
	thisMasterAngle = thisLayer.glyphMetrics()[5]
	myY = thisMasterAngle / 100 
	myX = -thisMasterAngle / 100 
	yShift.append(thisLayer.bounds.origin.y)
	xShift.append(thisLayer.bounds.origin.x)
	thisLayer.beginChanges()
	thisLayer.applyTransform([1, myX, myY*2, 1, 0, 0])
	thisLayer.addNodesAtExtremes()
	yShift.append(thisLayer.bounds.origin.y)
	xShift.append(thisLayer.bounds.origin.x)
	thisLayer.endChanges()

def compensate( thisLayer ):
	for thisPath in thisLayer.paths:
		for thisNode in thisPath.nodes:
			thisNode.y += abs(yShift[2])
			thisNode.x -= abs(xShift[2])

thisFont.disableUpdateInterface() # suppresses UI updates in Font View
print "*** Start Rounding Glyphs\n"

try: 
	for thisLayer in selectedLayers:
		if not (thisLayer.glyphMetrics()[5] > 0):
			print "Italic Angle should be greater than zero. Set Italic Angle in Font Master"
			break
		print "Rounding glyph '%s' -> " % (thisLayer.parent.name),
		process( thisLayer )
		yShift.append(yShift[1] - yShift[0])
		xShift.append(xShift[1] - xShift[0])
		compensate( thisLayer )
		print "y-shift: %s, x-shift: %s" % (abs(yShift[2]), xShift[2])
		thisLayer.syncMetrics()

	for thisLayer in selectedLayers[:-1]: # Last layer
  		print "Done. Clean up nodes if necessary."
except TypeError: 
	print "No glyphs selected. Select glyphs and rerun script."
print "\n***"

thisFont.enableUpdateInterface() # re-enables UI updates in Font View