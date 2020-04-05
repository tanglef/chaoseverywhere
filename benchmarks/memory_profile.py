import memory_profiler
import os
import matplotlib.pyplot as plt
import time
import numpy as np
import shutil
from mayavi import mlab

class Mandelbrot_disp:

    def __init__(self, x, y, facteur, t_max=100, precision=400):
        self.x = x
        self.y = y
        self.facteur = facteur
        self.t_max = t_max
        self.precision = precision

    @profile
    def mandelbrot(self):
        x, y, facteur, maxiteration, precision = self.x, self.y, self.facteur, \
        self.t_max, self.precision
        # définit l'espace avec une matrice
        X, Y = np.meshgrid(np.linspace(x-facteur, x+facteur, precision),
                           np.linspace(y-facteur, y+facteur, precision),
                           sparse=True)
        c = X+1j*Y  # nombre complex écrit avec des matrices
        z = c
        # matrice booléenne qui vérifie la condition sur (z_n)
        pasbornee = np.zeros(z.shape, dtype=bool)
        for _ in range(maxiteration):
            z = z**2+c
            matrice = abs(z) > 2  # condition sur le cercle
            nouvelle = matrice & ~pasbornee  # le ~est la négation logique
            pasbornee[nouvelle] = True
            # valeur arbitraire pour éviter les overflow je limite la valeur =>
            z[matrice] = 1
            # prévient le problème des deux ci-dessous
        return pasbornee

    @profile
    def mandel_loop(self, go_up=True, puiss=2):
        x, y = np.ogrid[self.x - self.facteur:self.x +
                        self.facteur:(self.precision * 1j),
                        self.y - self.facteur:self.y +
                        self.facteur:(self.precision * 1j)]
        c = x + 1j * y
        z = np.zeros(c.shape)
        mandel = np.zeros(c.shape)
        for i in range(self.t_max):
            z = z ** puiss + c
            if go_up:
                mandel += 1 / float(2 + i) * (z * np.conj(z) > 4)
            else:
                mandel[z*np.conj(z) > 4] = i
        return(mandel)

    @profile
    def disp_mandel(self):
        mandel = self.mandelbrot()
        plt.figure()
        plt.imshow(mandel, cmap='bone')  # interpolation induite
        plt.axis('off')

    @profile
    def anim_pics_mandel(self, go_up=True, puiss=2):
        mlab.figure(size=(800, 800))
        mandel = self.mandel_loop(go_up=go_up, puiss=puiss)
        mlab.surf(mandel, colormap='hot', warp_scale='auto', vmax=1.5)
        script_dir = os.path.dirname(__file__)
        results_dir = os.path.join(script_dir, 'Animations')
        if not os.path.isdir(results_dir):
            os.makedirs(results_dir)
        for t in range(0, 170, 1):
            mlab.view(elevation=180-t)
            imgname = os.path.join(results_dir, 'rotation' + str(t) + ".png")
            mlab.savefig(imgname)
        for t in range(0, 30, 1):
            mlab.view(distance=1000-5*t, elevation=180)
            imgname = os.path.join(results_dir,
                                   'rotation' + str(170+t) + ".png")
            mlab.savefig(imgname)
        mlab.close()
        shutil.rmtree(results_dir)

@profile
def logistic_draw(x0, r, iteration, points):
    """ This function is a first way to be able to draw the logistic function, the curve (y=x)
    and the intersections beetwen these two curves recursively.
    """
    x = np.linspace(0, 1, points)
    plt.figure()
    plt.plot(x, logistic(r, x))
    plt.plot(x, x)
    for _ in range(iteration):
        f_x0 = logistic(r, x0)
        plt.plot([x0, x0], [x0, f_x0],
                 color='red', alpha=0.3)  # vertical stairs
        plt.plot([x0, f_x0], [f_x0, f_x0],
                 color='red', alpha=0.3)  # horizontal stairs
        plt.plot([x0, f_x0], [f_x0, f_x0], 'o',
                 color='grey', alpha=0.4)  # intersections
        x0 = f_x0
    plt.close()

@profile
def logistic(r, x):
    return(r*x*(1-x))

if __name__ == "__main__":
    Mandelbrot_disp(-.5,0,1,100,400).mandelbrot()
    time.sleep(1)
    Mandelbrot_disp(-.5,0,1,100,400).mandel_loop()
    time.sleep(1)
    Mandelbrot_disp(-.5,0,1,100,400).disp_mandel()
    time.sleep(1)
    Mandelbrot_disp(-.5,0,1,100,400).anim_pics_mandel()
    time.sleep(1)    
    logistic_draw(.01,2.7,50,100)