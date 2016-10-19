#MenuTitle: Update WinAsc and WinDesc
'''
Update custom paramters WinAscender and WinDescender according to tallest glyphs

'''
#
# Based on scripts from Marc Foley
# https://github.com/m4rc1e/mf-glyphs-scripts
#
# Get tallest and deepest glyphs

font = Glyphs.font

tallest = 0
tallest_name = ''

deepest = 0 
deepest_name = ''
for i, master in enumerate(font.masters):
	for glyph in font.glyphs:
		height = glyph.layers[i].bounds[-1][-1]
		depth = glyph.layers[i].bounds[0][-1]
		
		if height > tallest:
			tallest = height
			tallest_name = glyph.name
		
		if depth < deepest:
			deepest = depth
			deepest_name = glyph.name

print 'deepest glyph is %s %s' % (deepest_name, deepest)
print 'tallest glyph = %s %s' % (tallest_name, tallest) 

masters = font.masters

for i,master in enumerate(masters):
    master.customParameters['winAscent'] = tallest
    master.customParameters['winDescent'] = abs(deepest)

print 'WinAscender = %s' % (tallest)
print 'WinDescender= %s' % (deepest)