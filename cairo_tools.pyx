#!/usr/bin/env python
#import cairo

cdef extern from "cairo.h":
    struct _cairo:
        pass
    ctypedef _cairo cairo_t
    
    struct cairo_status_t:
        pass
    
    enum cairo_path_data_type:
        CAIRO_PATH_MOVE_TO
        CAIRO_PATH_LINE_TO
        CAIRO_PATH_CURVE_TO
        CAIRO_PATH_CLOSE_PATH
    ctypedef cairo_path_data_type cairo_path_data_type_t
    
    struct inner_header:
        cairo_path_data_type_t type
        int length
        
    struct inner_point:
        double x,y
    
    union cairo_path_data_t:
        inner_header header
        inner_point point
    
    struct cairo_path_t:
        cairo_status_t status
        cairo_path_data_t *data
        int num_data

    void cairo_line_to(cairo_t *cr, double x, double y)
    void cairo_translate(cairo_t *cr, double x, double y)
    void cairo_append_path(cairo_t *cr, void *pth)
    
    
cdef extern from "pycairo.h":
    cairo_t* PycairoContext_GET(object)
    
cdef extern from "cairohelper.h":
    cairo_path_t* PycairoPath_GET(object)
    
    
import numpy as np
cimport numpy as np

def polyline(object cr, np.ndarray[np.double_t, ndim=1] ax,
                    np.ndarray[np.double_t, ndim=1] ay):
    cdef unsigned int nx=ax.shape[0]
    cdef unsigned int i
    cdef cairo_t* ctx = PycairoContext_GET(cr)
    if ay.shape[0] != nx:
        raise ValueError("X and Y arrays must have equal length")
    for i in xrange(nx):
        cairo_line_to(ctx, ax[i], ay[i])
        
        
def stamp_at(object cr, object path, np.ndarray[np.double_t, ndim=1] ax,
                    np.ndarray[np.double_t, ndim=1] ay):
    cdef unsigned int nx=ax.shape[0]
    cdef unsigned int i
    cdef double x,y
    cdef cairo_t *ctx = PycairoContext_GET(cr)
    cdef cairo_path_t *pth = PycairoPath_GET(path)
    if ay.shape[0] != nx:
        raise ValueError("X and Y arrays must have equal length")
    for i in xrange(nx):
        x = ax[i]
        y = ay[i]
        cairo_translate(ctx, x,y)
        cairo_append_path(ctx, pth)
        cairo_translate(ctx, -x,-y)
        