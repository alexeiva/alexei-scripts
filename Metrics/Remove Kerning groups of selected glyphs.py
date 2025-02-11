MenuTitle: Remove Kerning Groups from Selected Glyphs
# -*- coding: utf-8 -*-
import GlyphsApp

Font = Glyphs.font  # Get the current font
selectedLayers = Font.selectedLayers  # Get selected glyphs

count = 0
for layer in selectedLayers:
    glyph = layer.parent
    if glyph is not None:
        glyph.leftKerningGroup = None  # Remove left kerning group
        glyph.rightKerningGroup = None  # Remove right kerning group
        print(f"Removed kerning groups from: {glyph.name}")
        count += 1

Glyphs.showNotification(
    "Kerning Groups Removed",
    f"Removed kerning groups from {count} glyphs."
)

print(f"✅ Removed kerning groups from {count} selected glyphs.")