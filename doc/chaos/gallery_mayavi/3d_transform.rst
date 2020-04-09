The 3D-transformation
==========================

Some setup
--------------

.. code-block:: python

    import chaoseverywhere as chaos
    from mayavi import mlab
    import os


Transformed Mandelbrot set
--------------------------------

The Mandelbrot set is defined by its famous equation :math:`z_{n+1}=z_n^2+c`.
Now, what happens if we change that formula.

.. math::

   z_{n+1}=f(z_n,c)=\left(\dfrac{z_n^2+c-1}{2z_n+c-2}\right)^2,

with :math:`z_0=0\in\mathbb{C}`.

Construction
-----------------

First, we define the function :math:`f(z,c):\mathbb{C}\times\mathbb{C}\longrightarrow\mathbb{C}` as above.

.. code-block:: python

    def transform(z,c):
        return(((z ** 2 + c -1)/(2*z +c-2))**2)

Then, we use the Mandelbrot_disp class in this package to create a basis for the set, and then we use mayavi to display our work.

.. code-block:: python

    mandel = chaos.Mandelbrot_disp(1.5,0,2.5, precision=600).mandel_transform(FUN=transform)
    mlab.figure(size=(800, 800))
    mlab.surf(mandel, colormap='hot', warp_scale='auto', vmax=1.5)
    mlab.view(elevation=180)
    mlab.close()

.. raw:: html

    <img class='sphx-glr-single-img' src='../../../../../doc/_images/3d_transform.svg'/>

What are we looking at ?
-------------------------------

This transformation is called the Magnet (1) and represents the way magnets behave under high temperatures.
It was discovered by two physicits Yang and Lee who dit not expect to see a fractal in their study.
