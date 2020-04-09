"""
Creating the Mandelbrot Set with colors
=========================================

"""

########################
# Some setup
# --------------

import chaoseverywhere as chaos
import matplotlib.pyplot as plt

##################################
# Colored Mandelbrot
# --------------------------------
#
# The second easiest way to see the Mandelbrot is not only to consider the points which are in the set, but also categorize how fast the others diverge.
# It is well known that the Mandelbrot set is contained in the origin disk of radius 2 :math:`D((0,0),2)`, so we just iterate the formula :
#
# .. math::
#
#   z_{n+1}=z_n^2+c,\ c\in\mathbb{C},
#
# with :math:`z_0=0\in\mathbb{C}`. And the twist here is to change the value of the points whose modulus is beyond 2. Let's consider that we affect it with the value of the current iteration.
# For that and because it can be time consuming to calculate the modulus of numbers in an array (mainly because of the square root), we use the formula :
#
# .. math::
# 
#    \forall\ z \in\mathbb{C},\ |z|^2=z\bar{z}.
#
# And then, we don't compare it with 2, but :math:`2^2`.

mandel = chaos.Mandelbrot_disp(0,0,2,t_max=150).mandel_loop(go_up=False)
fig, ax = plt.subplots()
pict = ax.imshow(mandel, cmap='cool')
fig.colorbar(pict, extend='both')
plt.show()


########################################
# Not so good...
# -------------------------
#
# The issue here is that chosing the iteration number creates jumps that may be not the smoothest and because :math:`z_0=0` and some points take a lot of iterations to make the sequence diverge (the one near the boundary), the constrast is not really visible.
# In order to correct that, we have a lot of choices, let's take :math:`\frac{1}{2+n}`, where :math:`n` is the current iteration of the sequence.
# We can also see that the Mandelbrot set is symmetric with respect to the real axis.


mandel = chaos.Mandelbrot_disp(0,0,2,t_max=150).mandel_loop(go_up=True)
fig, ax = plt.subplots()
pict = ax.imshow(mandel, cmap='cool')
ax.axvline(x=200, color='black')
fig.colorbar(pict, extend='both')
plt.show()
