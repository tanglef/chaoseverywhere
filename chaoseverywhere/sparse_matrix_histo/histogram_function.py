import numpy as np
import matplotlib.pyplot as plt



def histogram(x=-.5, y=0, window=1.5):
    mandel = Mandelbrot_disp(-.5,0,1.5).mandel_loop()
    data = np.array(np.unique(mandel,return_counts=True)).T
    plt.style.use('ggplot')
    plt.figure()
    plt.bar(data[:,0],data:[:,1], width=.15, align= 'edge')
    plt.show()