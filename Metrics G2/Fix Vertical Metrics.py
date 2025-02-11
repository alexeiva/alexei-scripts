#MenuTitle: Fix vertical metrics
'''
Sets custom parameters for vertical metrics in all masters.
Replaces vertical metrics with values calculated from key glyphs.

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

print ''
print '#############################################'
print ''
print 'Tallest glyph is %s %s' % (tallest_name, tallest) 
print 'winAscent = %s' % tallest
print ' '
print 'Deepest glyph is %s %s' % (deepest_name, deepest)
print 'winDescent = %s' % abs(deepest)
print ''

# Update vertical metrics for each master individually

ASC_G = 'l'
CAP_G = 'H'
XHEIGHT_G = 'x'
DESC_G = 'p'

for i, master in enumerate(masters):
    n_asc = font.glyphs[ASC_G].layers[master.id].bounds[-1][-1] - abs(font.glyphs[ASC_G].layers[master.id].bounds[0][-1])
    n_cap = font.glyphs[CAP_G].layers[master.id].bounds[-1][-1]
    n_xhe = font.glyphs[XHEIGHT_G].layers[master.id].bounds[-1][-1]
    n_desc = font.glyphs[DESC_G].layers[master.id].bounds[0][-1]
    
    master.ascender = int(round(n_asc))
    master.capHeight = int(round(n_cap))
    master.xHeight = int(round(n_xhe))
    master.descender = int(round(n_desc))

## Update vertical metrics custom paramters for all master

for i, master in enumerate(masters):
    
    '''
    master.ascender = n_asc
    master.capHeight = n_cap
    master.xHeight = n_xhe
    master.descender = n_desc
    '''

    remainder = int( round( 1250 - abs(n_desc) - n_asc) )

    master.customParameters['winAscent'] = tallest
    master.customParameters['winDescent'] = abs(deepest)

    master.customParameters['typoAscender'] = n_asc+remainder
    master.customParameters['hheaAscender'] = n_asc+remainder
    
    master.customParameters['typoDescender'] = deepest
    master.customParameters['hheaDescender'] = deepest
    
    master.customParameters['hheaLineGap'] = 0
    master.customParameters['typoLineGap'] = 0
   
print ''
print '#############################################'
print ''
print 'New vertical metrics values for all masters:'
print ''
print '#############################################'
print ''
print 'winAscent = %s' % tallest
print 'winDescent = %s' % abs(deepest)
print ' '
print 'typoAscender = %s' % (n_asc+remainder)
print 'hheaAscender = %s' % (n_asc+remainder)
print ' '
print 'typoDescender = %s' % deepest
print 'hheaDescender = %s' % deepest
print ' '
print 'hheaLineGap = 0'
print 'typoLineGap = 0'
print ''
print 'Vertical metrics updated according to 125 %% rule'
print ''
