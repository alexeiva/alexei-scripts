#MenuTitle: Test modules import
'''
Tests importing modules
'''
#
# based code by @mekkablue
#

from AppKit import * 
import GlyphsApp, sys, os, math
print "-- System: %s" % sys.version
print "-- OS: %s; %s" % ( os.name, os.uname() )
for infoKey in ("CFBundleShortVersionString", "CFBundleVersion"):
	print "-- App %s: %s" % ( infoKey, NSBundle.bundleForClass_(GSMenu).infoDictionary().objectForKey_(infoKey) ) 
import vanilla
import fontTools
#import dialogKit
import robofab
print "-- Vanilla: %s" % vanilla
print "-- fontTools: %s" % fontTools
#print "-- dialogKit: %s" % dialogKit
print "-- robofab: %s" % robofab