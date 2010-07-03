#!/usr/bin/env python
#import cairo

cdef extern from "cairo.h":
    void cairo_line_to(void *cr, double x, double y)
    void cairo_translate(void *cr, double x, double y)
    void cairo_append_path(void *cr, void *pth)
    
cdef extern from "pycairo.h":
    ctypedef class cairo.Context [object PycairoContext]:
        cdef int ctx
        cdef object base
        
    ctypedef class cairo.Path [object PycairoPath]:
        cdef int path
    
import numpy as np
cimport numpy as np

def polyline(Context cr, np.ndarray[np.double_t, ndim=1] ax,
                    np.ndarray[np.double_t, ndim=1] ay):
    cdef unsigned int nx=ax.shape[0]
    cdef unsigned int i
    cdef void *ctx = <void*>cr.ctx
    if ay.shape[0] != nx:
        raise ValueError("X and Y arrays must have equal length")
    for i in xrange(nx):
        cairo_line_to(ctx, ax[i], ay[i])
        
def stamp_at(Context cr, Path path, np.ndarray[np.double_t, ndim=1] ax,
                    np.ndarray[np.double_t, ndim=1] ay):
    cdef unsigned int nx=ax.shape[0]
    cdef unsigned int i
    cdef double x,y
    cdef void *ctx = <void*>cr.ctx
    cdef void *pth = <void*>path.path
    if ay.shape[0] != nx:
        raise ValueError("X and Y arrays must have equal length")
    for i in xrange(nx):
        x = ax[i]
        y = ay[i]
        cairo_translate(ctx, x,y)
        cairo_append_path(ctx, pth)
        cairo_translate(ctx, -x,-y)