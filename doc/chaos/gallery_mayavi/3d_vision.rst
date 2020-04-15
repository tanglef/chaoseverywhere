The Mandelbrot set with three dimensions
========================================

Some setup
--------------

.. code-block:: python

    import chaoseverywhere as chaos
    from mayavi import mlab

Is it really a fractal in 3-dimensional fractal ?
-----------------------------------------------------------

The Mandelbrot set is defined by its famous equation :math:`z_{n+1}=z_n^2+c`.
Having a 3-dimensional visualization of this set is very complex and to be considered a 3D fractal, we need to keep the fractal part of the object.
We often consider the Mandelbulb as the 3-dimensional representation of the Mandelbrot set. However, we can't make a 3D Mandelbrot set in the way
we'd like to be. So in this package you won't be able to see a Mandelbulb or some bootleg version of that can be found of it. Here we will only
use the third dimension to see the speed of divergence of the points.

Construction
-----------------

First, we define the function of the Mandelbrot set :math:`f(z,c):\mathbb{C}\times\mathbb{C}\longrightarrow\mathbb{C}` as above.

.. code-block:: python

    def transform(z,c):
        return(z**2 + c)

Then, we use the Mandelbrot_disp class in this package to create a basis for the set, and then we use mayavi to display our work.

.. code-block:: python

    mandel = chaos.Mandelbrot_disp(1.5,0,2.5, precision=600).mandel_transform(FUN=transform)
    mlab.figure(size=(800, 800))
    mlab.surf(mandel, colormap='bones', warp_scale='auto', vmax=1.5)
    mlab.view(elevation=18)
    mlab.close()

.. raw:: html

    <img class='sphx-glr-single-img' src='../../_images/3d_vision.svg'/>



The hidden part of the iceberg
----------------------------------

We can clearly see the different speed of divergence, so let's take a look around them. On one side we see the points inside the Mandelbrot
set and we can observe a denser part at the extrimity along the the real axis. On the flipped side, we can see that there is a sharp
contrast between the speed of divergence of most of the points, and the one the nearest to boundary.

.. raw:: html

     <iframe width="356" height="200" src="https://www.youtube.com/embed/watch?v=Wr0_-8X_AfE&list=UUdnqdTeUXeMNaeVrbCnxKkA&index=1" frameborder="0" allowfullscreen></iframe>


You can produce the same animation using the code below.

.. code-block:: python

    chaos.Mandelbrot_disp(-.5,0,1.5, 200,500).anim_pics_mandel(go_up=False)