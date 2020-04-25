How to install chaoseverywhere
=================================

.. role:: bash(code)
   :language: bash

Install from github
^^^^^^^^^^^^^^^^^^^^^^

In order to install this package, one can simply put in the prompt:

.. code-block:: bash

    $ pip install git+https://github.com/tanglef/chaoseverywhere


Special dependencies
^^^^^^^^^^^^^^^^^^^^^^

In order to fully use this package, one must have Mayavi installed and ready to use and also the FFMPEG writer.

* Mayavi: VTK and PyQt5 (or another supported GUI toolkit for Python 3) are necessary please refer to `this tutorial`_.
* FFMPEG: simply run :bash:`sudo apt install ffmpeg` if you're using a UBUNTU distribution.

.. _this tutorial: https://docs.enthought.com/mayavi/mayavi/installation.html

.. Tip::

    If you're using Windows, you will need to install FFMPEG by downloading the folder of the latest version,
    save it where you'd like (usually the root of the disk) and add the path to its ``bin`` folder to the PATH environment variables.
    If you're using Windows 7/8, add a semicolon at the end of the added path. 


Once you're done, you can test your installation by running the ``plot_bifurcation.py`` file in the ``\examples`` directory.