Chaning the power in the equation
========================================

Some setup
--------------

.. code-block:: python

    import chaoseverywhere as chaos
    from mayavi import mlab

An example with a power of 4
-----------------------------------------------------------

The Mandelbrot set is defined by its famous equation :math:`z_{n+1}=z_n^2+c`.
But one could rightfully ask : why :math:`2` exactly ?
So let's fulfill our curious needs and see what happens if we take :math:`z_{n+1}=z_n^4+c` as our equation.

Construction
-----------------

First, we define the function of the Mandelbrot set :math:`f(z,c):\mathbb{C}\times\mathbb{C}\longrightarrow\mathbb{C}` as above.

.. code-block:: python

    def transform(z,c):
        return(z**4 + c)

Then, we use the Mandelbrot_disp class in this package to create a basis for the set, and then we use mayavi to display our work.

.. code-block:: python

    mandel = chaos.Mandelbrot_disp(1.5,0,2.5, precision=600).mandel_transform(FUN=transform)
    mlab.figure(size=(800, 800))
    mlab.surf(mandel, colormap='hot', warp_scale='auto', vmax=1.5)
    mlab.view(elevation=18)
    mlab.close()

.. raw:: html

    <img class='sphx-glr-single-img' src='../../_images/puiss4.svg'/>


We can clearly see some king of duplicates into three of Mandelbrot sets displaying themselves around the main bulb and allowing for each
of them a third of the space to grow.

And for the other powers ?
----------------------------------
For a power of :math:`2`, we see one big ramification extending over the real axis. For a power of :math:`4` we see three of them.
So we can conjecture that for any positive integer :math:`p` as the power, we will see :math:`p-1` main ramifications around the main bulb.
Let's see if that checks out for the first hundred powers.

.. raw:: html

     <iframe width="356" height="200" src="https://www.youtube.com/embed/watch?v=Wr0_-8X_AfE&list=UUdnqdTeUXeMNaeVrbCnxKkA&index=3" frameborder="0" allowfullscreen></iframe>


One can reproduce this animation using the code below.

.. code-block:: python

    chaos.Mandelbrot_disp(0,0,2,t_max=150, precision=500).anim_puiss_mandel(remove=True)