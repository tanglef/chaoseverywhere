The Mandelbrot set
=========================

The creation
--------------------

The Mandelbrot set :math:`\mathcal{M}` is defined as :

.. math::

   \mathcal{M}=\left\{ c\in\mathbb{C},\ (z_n)_n \text{ is bounded},\ \text{with } z_{n+1}=z_n^2+c,\ z_0=0\right\}.


Given the fact that it is a set of points, we can compute it using a ``class`` Python object. Thus, determine which arguments to pass
in order to instantiate one set, and what methods to compute. What a user (you hopefully) might want to ask oneself is:

* where should I center the picture of the Mandelbrot set?
* do I want the whole set or just a special part? If the latest, what square exactly would I want to look at?
* do I need of lot of iterations of the sequence: meaning more time to make, or can I be satisfied with a reasonable number of iterations?

.. note::
   For only aesthetics purposes, we chose not to let the user display a rectangular part of the Mandelbrot set but only a square one.

   So, the windows that will be displayed will be a square centered at the point :math:`a+bi`. The user will input this point separating
   the real part and the imaginary part in the two arguments ``x`` and ``y``. The size of the square is determined by the ``facteur``
   argument representing the half-length of the side of the square one'd like to display.


A summary to keep in mind
-----------------------------

.. raw:: html

   <style type="text/css">
   .tg  {border-collapse:collapse;border-spacing:0;border-color:#aabcfe;}
   .tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 18px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#aabcfe;color:#669;background-color:#e8edff;}
   .tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 18px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#aabcfe;color:#039;background-color:#b9c9fe;}
   .tg .tg-phtq{background-color:#D2E4FC;border-color:inherit;text-align:left;vertical-align:top}
   .tg .tg-hmp3{background-color:#D2E4FC;text-align:left;vertical-align:top}
   .tg .tg-baqh{text-align:center;vertical-align:top}
   .tg .tg-0lax{text-align:left;vertical-align:top}
   .tg .tg-j0tj{background-color:#D2E4FC;text-align:center;vertical-align:top}
   .tg .tg-svo0{background-color:#D2E4FC;border-color:inherit;text-align:center;vertical-align:top}
   </style>
   <p>
   <table class="tg">
     <tr>
       <th class="tg-0lax">Methods</th>
       <th class="tg-baqh" colspan="3">Output</th>
     </tr>
     <tr>
       <td class="tg-hmp3"></td>
       <td class="tg-j0tj">numpy array</td>
       <td class="tg-j0tj">saved video</td>
       <td class="tg-j0tj">matplotlib plot</td>
     </tr>
     <tr>
       <td class="tg-0lax">anim_puiss_mandel</td>
       <td class="tg-baqh"></td>
       <td class="tg-baqh">X</td>
       <td class="tg-baqh"></td>
     </tr>
     <tr>
       <td class="tg-phtq">anim_pics_mandel</td>
       <td class="tg-svo0"></td>
       <td class="tg-j0tj">X</td>
       <td class="tg-svo0"><br></td>
     </tr>
     <tr>
       <td class="tg-0lax">animate_mandel_plt</td>
       <td class="tg-baqh"></td>
       <td class="tg-baqh">X</td>
       <td class="tg-baqh"></td>
     </tr>
     <tr>
       <td class="tg-hmp3">disp_mandel</td>
       <td class="tg-j0tj"></td>
       <td class="tg-j0tj"></td>
       <td class="tg-j0tj">X</td>
     </tr>
     <tr>
       <td class="tg-0lax">mandel_loop</td>
       <td class="tg-baqh">X</td>
       <td class="tg-baqh"></td>
       <td class="tg-baqh"></td>
     </tr>
     <tr>
       <td class="tg-hmp3">mandel_transform</td>
       <td class="tg-j0tj">X</td>
       <td class="tg-j0tj"></td>
       <td class="tg-j0tj"></td>
     </tr>
     <tr>
       <td class="tg-0lax">mandelbrot<br></td>
       <td class="tg-baqh">X</td>
       <td class="tg-baqh"></td>
       <td class="tg-baqh"></td>
     </tr>
   </table>
   </br>
   </p>




The class methods
-------------------------

.. autoclass:: chaoseverywhere.mandel.create_mandel.Mandelbrot_disp
   :members:


Additional function in the submodule
----------------------------------------
As part of the link with the logistic map, we needed a function that could return a stairs-like data about the different
values that would take the map :math:`z_{n+1}=z_n^2+c` with different values for :math:`c`. See the bifurcation video in the gallery
for the actual plot.

.. autofunction:: chaoseverywhere.mandel.create_mandel.mandel_branch_points


One can use this function to produce the same plot in the top-right of the video in the bifurcation diagram section of the gallery using the code below.

.. code-block:: python

   plt.style.use(['ggplot', 'dark_background'])

   data = zip(*chaos.mandel_branch_points(0,-1,50))
   ax2 = plt.subplot()
   x = np.linspace(-2, 1, 400)

   line, = ax2.plot([],[], color='red', alpha=1, lw=4)
   line.set_data(data)
   
   courbe, = ax2.plot([], [], color='dodgerblue', alpha=1, lw=2)
   courbe.set_data(x, x**2-1)
   ax2.plot(x, x, color='orange')
   plt.show()




