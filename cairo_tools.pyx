#!/usr/bin/env python
#import cairo

cdef extern from "cairo.h":
    void cairo_line_to(void *cr, double x, double y)
    
cdef extern from "pycairo.h":
    ctypedef class cairo.Context [object PycairoContext]:
        cdef int ctx
        cdef object base
    

def list_to_path(Context cr, list points):
    cdef double x,y
    for x,y in points:
        cairo_line_to(<void *>cr.ctx, x, y)
        
        