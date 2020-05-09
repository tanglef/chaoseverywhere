import numpy as np
import matplotlib.pyplot as plt
from chaoseverywhere.sparse_matrix_histo import Mandelbrot_disp

def histogram(x=-.5, y=0, window=1.5):
    """Creates a histogram.

    Histogram display for each color density.

    :param x: coordinate for the points of mandelbrot set
    :type x: float
    :param y: coordinate for the points of mandelbrot set
    :type y: float
    :param window: size of the viewing window
    :type window: float
    :return: histogram
    :rtype: matplotlib plot
    """
    mandel = Mandelbrot_disp(x, y, window).mandel_loop()
    data = np.array(np.unique(mandel,return_counts=True)).T
    plt.style.use('ggplot')
    plt.figure()
    plt.bar(data[:,0],data[:,1], width=.15, align= 'edge')
    plt.show()