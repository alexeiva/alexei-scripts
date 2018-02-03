#MenuTitle: Delete orphan layers
# -*- coding: utf-8 -*-
__doc__="""
Delete orphan layers in selected
"""

thisFont = Glyphs.font # frontmost font
thisFontMaster = thisFont.selectedFontMaster # active master
selectedLayers = thisFont.selectedLayers # active layers of selected glyphs

def process( thisLayer ):

	for thisLayer in selectedLayers:
		for l in thisLayer.parent.layers:
			if l.name == None or l.name != 'Bold Italic':
				deleteId = l.layerId
				del(thisFont.glyphs[thisLayer.parent.name].layers[deleteId])
				print "Deleted orphan layer in glyph %s." % (thisLayer.parent.name)

thisFont.disableUpdateInterface() # suppresses UI updates in Font View

process( thisLayer )

thisFont.enableUpdateInterface() # re-enables UI updates in Font View
