"""
Creating the classic Mandelbrot set
======================================

"""

########################
# Some setup
# --------------

import chaoseverywhere as chaos

##################################
# Classic Mandelbrot
# --------------------------------
#
# First, let's compute the classic version of the mandelbrot set in black and white.
# It is well known that the Mandelbrot set is contained in the origin disk of radius 2 :math:`D((0,0),2)`, so we just iterate the formula :
#
# .. math::
#
#   z_{n+1}=z_n^2+c,\ c\in\mathbb{C},
#
# with :math:`z_0=0\in\mathbb{C}`.

chaos.Mandelbrot_disp(0,0,2,t_max=150).disp_mandel()