#MenuTitle: Fix vertical metrics
'''
Sets custom parameters for vertical metrics in all masters.
Replace vertical metrics with values calculated from key glyphs.

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

# update values for masters

ASC_G = 'l'
CAP_G = 'H'
XHEIGHT_G = 'x'
DESC_G = 'p'

masters = font.masters

for i,master in enumerate(masters):
    n_asc = font.glyphs[ASC_G].layers[master.id].bounds[-1][-1] - abs(font.glyphs[ASC_G].layers[master.id].bounds[0][-1])
    n_cap = font.glyphs[CAP_G].layers[master.id].bounds[-1][-1]
    n_xhe = font.glyphs[XHEIGHT_G].layers[master.id].bounds[-1][-1]
    n_desc = font.glyphs[DESC_G].layers[master.id].bounds[0][-1]
    
    master.ascender = n_asc
    master.capHeight = n_cap
    master.xHeight = n_xhe
    master.descender = n_desc
    master.customParameters['winAscent'] = tallest
    master.customParameters['typoAscender'] = tallest
    master.customParameters['hheaAscender'] = tallest
    master.customParameters['typoDescender'] = deepest
    master.customParameters['hheaDescender'] = deepest
    master.customParameters['winDescent'] = abs(n_desc)
    master.customParameters['hheaLineGap'] = 0
    master.customParameters['typoLineGap'] = 0
   
print 'Vertical metrics updated'
