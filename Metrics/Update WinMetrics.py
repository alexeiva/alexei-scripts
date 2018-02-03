#MenuTitle: Update winAsc and winDesc
'''
Update custom paramters winAscender and winDescender

'''
#
# Based on scripts from Marc Foley
# https://github.com/m4rc1e/mf-glyphs-scripts
#

font = Glyphs.font

tallest = 0
tallest_name = ''

deepest = 0 
deepest_name = ''

masters = font.masters

for i, master in enumerate(masters):
	for glyph in font.glyphs:
		height = glyph.layers[i].bounds[-1][-1]
		depth = glyph.layers[i].bounds[0][-1]
		
		if height > tallest:
			tallest = height
			tallest_name = glyph.name
		
		if depth < deepest:
			deepest = depth
			deepest_name = glyph.name

tallest = int( round(tallest) ) 
deepest = int( round(deepest) ) 

print 'tallest glyph is %s %s' % (tallest_name, tallest) 
print 'winAscent = %s %s' % (tallest_name, round(tallest) ) 
print ' '
print 'deepest glyph is %s %s' % (deepest_name, deepest)
print 'winDescent = %s %s' % (deepest_name, int( round (abs(deepest)) ))

for i, master in enumerate(masters):
    master.customParameters['winAscent'] = tallest
    master.customParameters['winDescent'] = deepest