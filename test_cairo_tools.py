#!/usr/bin/env python

import cairo
import cairo_tools
from math import sin

surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, 400,400)
ctx = cairo.Context(surf)
ctx.set_source_rgb(1.0,0,0)
ctx.scale(400,400)
data = [(x/1000., 0.5+sin(x/20.)/2.) for x in xrange(1000)]
cairo_tools.list_to_path(ctx, data)
ctx.set_line_width(0.01)
ctx.stroke()
surf.write_to_png("test_image.png")

print "end"
