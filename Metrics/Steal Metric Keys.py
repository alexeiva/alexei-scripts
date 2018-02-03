#MenuTitle: Steal Metrics Keys from font
"""Copy Metrics Keys from one font to another."""
# Based on 'Steal kerning groups from font' by @mekkablue
import vanilla

class KeysCopy(object):
	"""GUI for copying Metrics Keys from one font to another"""
	def __init__(self):
		self.w = vanilla.FloatingWindow((400, 70), "Steal Metrics Keys")
		
		self.w.text_anchor = vanilla.TextBox((15, 12+2, 130, 14), "Copy keys from:", sizeStyle='small')
		self.w.from_font = vanilla.PopUpButton((150, 12, 150, 17), self.GetFonts(isSourceFont=True), sizeStyle='small', callback=self.buttonCheck)
		
		self.w.text_value = vanilla.TextBox((15, 12+2+25, 130, 14), "To selected glyphs in:", sizeStyle='small')
		self.w.to_font = vanilla.PopUpButton((150, 12+25, 150, 17), self.GetFonts(isSourceFont=False), sizeStyle='small', callback=self.buttonCheck)

		self.w.copybutton = vanilla.Button((-80, 12+25, -15, 17), "Copy", sizeStyle='small', callback=self.copyKeys)
		self.w.setDefaultButton( self.w.copybutton )

		self.w.open()
		self.buttonCheck(None)
		
	def GetFonts(self, isSourceFont):
		myFontList = [ "%s - %s" % ( x.font.familyName, x.selectedFontMaster().name ) for x in Glyphs.orderedDocuments() ]

		if isSourceFont:
			myFontList.reverse()
		
		return myFontList
	
	def buttonCheck(self, sender):
		fromFont = self.w.from_font.getItems()[ self.w.from_font.get() ]
		toFont   = self.w.to_font.getItems()[ self.w.to_font.get() ]

		if fromFont == toFont:
			self.w.copybutton.enable( onOff=False )
		else:
			self.w.copybutton.enable( onOff=True )
	
	def copyKeys(self, sender):
		fromFont = self.w.from_font.getItems()[ self.w.from_font.get() ]
		toFont   = self.w.to_font.getItems()[ self.w.to_font.get() ]
		
		Doc_source      = [ x for x in Glyphs.orderedDocuments() if ("%s - %s" % ( x.font.familyName, x.selectedFontMaster().name )) == fromFont ][0]
		Master_source   = Doc_source.selectedFontMaster().id
		Font_source     = Doc_source.font
		Font_target     = [ x.font for x in Glyphs.orderedDocuments() if ("%s - %s" % ( x.font.familyName, x.selectedFontMaster().name )) == toFont ][0]
		Glyphs_selected = [ x.parent for x in Font_target.parent.selectedLayers() ]
		
		print "Syncing metrics keys for", len(Glyphs_selected), "glyphs from", Font_source.familyName, "to", Font_target.familyName, ":"
		
		try:
			for thisGlyph in Glyphs_selected:
					glyphName = thisGlyph.name
					try:
						sourceGlyph = Font_source.glyphs[ glyphName ]
						oldL = thisGlyph.leftMetricsKey
						oldR = thisGlyph.rightMetricsKey
						newL = sourceGlyph.leftMetricsKey
						newR = sourceGlyph.rightMetricsKey
						
						if oldL != newL or oldR != newR:
							thisGlyph.leftMetricsKey  = newL
							thisGlyph.rightMetricsKey = newR
							
							print "   ", glyphName, ":", newL, "<--->", newR
							print "Syncing metrics..."

							myLayers = Glyphs.font.selectedLayers
							for thisLayer in myLayers:
								thisLayer.syncMetrics()
							
						pass
					except Exception, e:
						print "   ", glyphName,": Error"
						# print e

		except Exception, e:
			self.showMessage( "Error", e )
		
		finally:
			print "Done."

		self.w.close()
		
KeysCopy()
