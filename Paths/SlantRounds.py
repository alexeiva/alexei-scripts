#MenuTitle: Slant Rounds
# -*- coding: utf-8 -*-
# The slanting algorithm is based on
# method by Jacques Le Bailly <fonthausen@baronvonfonthausen.com>
# Copyright 2017 Alexei Vanyashin <a@cyreal.org>
__doc__="""
Slants round glyphs with vertical compensation. Based on method by Jacques Le Bailly
"""

import GlyphsApp
thisMasterAngle = thisLayer.glyphMetrics()[5]
myY = thisMasterAngle / 100 
myX = -thisMasterAngle / 100 
compensationAmount = 9

thisFont = Glyphs.font # frontmost font
selectedLayers = thisFont.selectedLayers # active layers of selected glyphs


def process( thisLayer ):

	for thisLayer in selectedLayers:
	
		bounds = thisLayer.bounds
		minY = bounds.origin.y
		minX = bounds.origin.x
		offsetY = + compensationAmount - minY
		offsetX = + compensationAmount - minX

		thisLayer.beginChanges()
		thisLayer.applyTransform([1, myX, myY*2, 1, offsetX, offsetY])
		thisLayer.addNodesAtExtremes()
		thisLayer.setColorIndex_(1)
		thisLayer.syncMetrics()
		thisLayer.endChanges()

thisFont.disableUpdateInterface() # suppresses UI updates in Font View

process( thisLayer )

for thisLayer in selectedLayers:
	print "Processing %s" % thisLayer.parent.name
	thisLayer.syncMetrics()

thisFont.enableUpdateInterface() # re-enables UI updates in Font View

Glyphs.clearLog()
Glyphs.showMacroWindow()
