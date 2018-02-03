#MenuTitle: Set Metrics Keys Auto
# encoding: utf-8
# Based on script by Georg Seifert
# Copyright: Georg Seifert, 2010, www.schriftgestaltung.de Version 1.0
import sys
import os
from GlyphsApp import *
import objc
from AppKit import *
from Foundation import *
import traceback


def KeysForGlyph(Glyph):
	if Glyph == None:
		return []
	global DefaultKeys
	LeftKey = False
	RightKey = False
	try:
		LeftKey = Glyph.leftMetricsKey
	except:
		print traceback.format_exc()
	try:
		RightKey = Glyph.rightMetricsKey
	except:
		print traceback.format_exc()
	try:
		if len(LeftKey < 1):
			LeftKey = False
	except TypeError:
		pass
	except:
		print traceback.format_exc()
	try:
		if len(RightKey < 1):
			RightKey = False
	except TypeError:
		pass
	except:
		print traceback.format_exc()
	return (LeftKey, RightKey)

def updateKeyGlyphsForSelected():
	Doc = Glyphs.currentDocument
	Font = Doc.font
	SelectedLayers = Doc.selectedLayers()
	for Layer in SelectedLayers:
		Glyph = Layer.parent
		LeftKey = ""
		RightKey = ""
		LigatureComponents = Glyph.name.split("_")
		if len(Layer.components) > 0 and len(Layer.paths) == 0 and Layer.components[0].transformStruct()[0] == 1:
			componentGlyph = Layer.components[0].component
			if not componentGlyph:
				raise Exception("Something is wrong with a Component in Glyphs %s" % Layer.parent.name)
			if componentGlyph.category == "Letter":
				LeftKey = KeysForGlyph(componentGlyph)[0]
			if not LeftKey:
				LeftKey = componentGlyph.name
			
			for Component in Layer.components:
				try:
					if Component.component.category == "Letter":
						if Component.transform[0] == 1:
							componentGlyph = Component.component
					elif Component.component.category != "Mark":
						#componentGlyph = None
						pass
				except:
					pass
			if componentGlyph:
				RightKey = KeysForGlyph(componentGlyph)[1]
				if not RightKey:
					RightKey = componentGlyph.name
		
		elif len(LigatureComponents) > 1:
			LeftGlyph = Font.glyphs[LigatureComponents[0]]
			if LeftGlyph != None:
				LeftKey = KeysForGlyph(LeftGlyph)[0]
			RightGlyph = Font.glyphs[LigatureComponents[-1]]
			if RightGlyph != None:
				RightKey = KeysForGlyph(RightGlyph)[1]
		if LeftKey:
			try:
				if LeftKey not in Font.glyphs and not Font.glyphs[LeftKey].export:
					LeftKey = False
			except:
				LeftKey = False
		if RightKey:
			try:
				if RightKey not in Font.glyphs and not Font.glyphs[RightKey].export:
					RightKey = False
			except:
				pass
		if not LeftKey:
			try:
				LeftKey = DefaultKeys[Glyph.name][0]
			except KeyError:
				pass
			except:
				print traceback.format_exc()
		if not RightKey:
			try:
				RightKey = DefaultKeys[Glyph.name][1]
			except KeyError:
				pass
			except:
				print traceback.format_exc()
		if not LeftKey and Glyph.name[-3:] == ".sc":
			try:
				Glyph
				LeftKey = DefaultKeys[Glyph.name[:-3].title()][0]
				if (len(LeftKey) > 0):
					LeftKey = LeftKey.lower()+".sc"
			except:
				print traceback.format_exc()
		if not RightKey and Glyph.name[-3:] == ".sc":
			try:
				RightKey = DefaultKeys[Glyph.name[:-3].title()][1]
				if (len(RightKey) > 0):
					RightKey = RightKey.lower()+".sc"
			except:
				print traceback.format_exc()
		if not LeftKey:
			LeftKey = Glyph.name
		if not RightKey:
			RightKey = Glyph.name
		
		print Glyph.name, ">", LeftKey, RightKey
		if Glyph.leftMetricsKey is None or len(Glyph.leftMetricsKey) == 0:
			Glyph.setLeftMetricsKey_(LeftKey)
		if Glyph.rightMetricsKey is None or len(Glyph.rightMetricsKey) == 0:
			Glyph.setRightMetricsKey_(RightKey)

def main():
 	print "Starting Metrics Keys update\n"
	updateKeyGlyphsForSelected()
	Doc = Glyphs.currentDocument
	Font = Doc.font
	SelectedLayers = Doc.selectedLayers()
	for Layer in SelectedLayers:
		Layer.syncMetrics()
	print "End"
	
def test():
	NewDefaultKeys = {}
	for key in Keys:
		key = niceName(key)
		values = DefaultKeys[key]
		newValues = []
		for value in values:
			newValues.append( niceName(value) )
		print "	\"%s\" : [\"%s\", \"%s\"]," % (key, newValues[1], newValues[0])
		NewDefaultKeys[key] = newValues
	#print NewDefaultKeys
main()
