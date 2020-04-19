Some other requirements for the project
-------------------------------------------

Sparse matrix
^^^^^^^^^^^^^^^

Sparse matrix are very efficient when we need to use a matrix with a lot of zeros-values.
To illustrate its use, we need a function that will randomly spread numbers with a chosen density.

.. automodule:: chaoseverywhere.sparse_matrix_histo.code_sparse
   :members:


Pixel colors
^^^^^^^^^^^^^^^

When we use the ``mandel_loop`` function, one can visualize the speed of divergence of the :math:`(z_n)_n` sequence.
We built an histogram representing each color for the speed of divergence on the :math:`(0,x)` axis and the associated
number of pixels in a chosen window on the :math:`(0,y)` axis.

.. automodule:: chaoseverywhere.sparse_matrix_histo.histogram_function
   :members: