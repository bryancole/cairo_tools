#!/usr/bin/env python
#import cairo

#cdef extern from "cairo.h":
#    void cairo_line_to(void *cr, double x, double y)
    
cdef extern from "pycairo.h":
    ctypedef class cairo.Context [object PycairoContext]:
        cdef void *ctx
    
import cairo
def list_to_path(cairo.Context cr, list points):
    print int(cr.ctx)