#!/usr/bin/env python

import cairo
import cairo_tools
import numpy

surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, 400,400)
ctx = cairo.Context(surf)
ctx.set_source_rgb(1.0,0,0)
ctx.scale(400,400)

x = numpy.linspace(0,1,1000)
y = 0.5 + numpy.sin(x*5)/2.

cairo_tools.polyline(ctx, x, y)
ctx.set_line_width(0.01)
path = ctx.copy_path()
print path
ctx.stroke()
surf.write_to_png("test_image.png")

print "end"
