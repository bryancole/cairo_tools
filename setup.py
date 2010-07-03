#!/usr/bin/env python
from distribute_setup import use_setuptools
use_setuptools()

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

#from setuptools import setup

ext_modules = [Extension("cairo_tools", ["cairo_tools.pyx"],
                    include_dirs=["/usr/include/pycairo",
                                "/usr/include/cairo",
                                "/usr/lib/python2.6/site-packages/numpy/core/include"],
                    libraries=['cairo']
                        )
                ]

setup(name='cairo_tools',
      version='0.1.0',
      description='utilities for enhancing pycairo',
      author='Bryan Cole',
      author_email='bryancole.cam@googlemail.com',
      url='',
      cmdclass = {'build_ext': build_ext},
      ext_modules = ext_modules,
      classifiers=['Development Status :: 3 - Alpha',
                'Intended Audience :: Developers',
                'License :: OSI Approved :: Python Software Foundation License',
                'Natural Language :: English',
                'Operating System :: OS Independent',
                'Programming Language :: Python :: 2.6',
                'Topic :: Utilities'
            ]
     )
