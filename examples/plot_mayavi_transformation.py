"""
Creating a 3D transformation of the Mandelbrot set
=====================================================

"""

########################
# Some setup
# --------------

import chaoseverywhere as chaos
from mayavi import mlab
import os

##################################
# Transformed Mandelbrot set
# --------------------------------
#
# The Mandelbrot set is defined by its famous equation :math:`z_{n+1}=z_n^2+c`.
# Now, what happens if we change that formula.
#
# .. math::
#
#   z_{n+1}=f(z_n,c)=\left(\dfrac{z_n^2+c-1}{2z_n+c-2}\right)^2,
#
# with :math:`z_0=0\in\mathbb{C}`.

######################
# Construction
# -----------------
# First, we define the function :math:`f(z,c):\mathbb{C}\times\mathbb{C}\longrightarrow\mathbb{C}` as above.

def transform(z,c):
    return(((z ** 2 + c -1)/(2*z +c-2))**2)

#####################
# Then, we use the Mandelbrot_disp class in this package to create a basis for the set, and then we use mayavi to display our work.
#

mlab.options.offscreen = True
mandel = chaos.Mandelbrot_disp(1.5,0,2.5, precision=600).mandel_transform(FUN=transform)

f=mlab.figure(size=(800, 800))
f.scene.disable_render = True
mlab.surf(mandel, colormap='hot', warp_scale='auto', vmax=1.5)
mlab.view(elevation=180)

save_folder = '../doc/_build/html/_images/'
os.makedirs(save_folder, exist_ok=True)
mlab.savefig(save_folder + '3d_transform.png')
mlab.close()

#############################
# .. raw:: html
#
#     <img class='sphx-glr-single-img' src='../../html/_images/3d_transform.png'/>
#

##########################
# What are we looking at ?
# -------------------------------
# This transformation is called the Magnet (1) and represents the way magnets behave under high temperatures.
# It was discovered by two physicits Yang and Lee who dit not expect to see a fractal in their study.
