import numpy as np
import ffmpeg
import matplotlib.pyplot as plt
from mayavi import mlab
import matplotlib.animation as animation
import os

class Mandelbrot_disp:

    def __init__(self, x, y, facteur, t_max=100, precision=400):
        self.x = x
        self.y = y
        self.facteur = facteur
        self.t_max = t_max
        self.precision = precision

    def mandelbrot(self):
        x, y, facteur, maxiteration, precision = self.x, self.y, self.facteur, self.t_max, self.precision
        # définit l'espace avec une matrice
        X, Y = np.meshgrid(np.linspace(x-facteur, x+facteur, precision),
                           np.linspace(y-facteur, y+facteur, precision), sparse=True)
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
        return pasbornee  # renvoi de la matrice booleenne qui indique si la valeur est bornée


    def disp_mandel(self):
        mandel = self.mandelbrot()
        plt.figure()
        plt.imshow(mandel, cmap='bone')  # interpolation induite
        plt.axis('off')
        plt.show()

    def animate_mandel_plt(self):
        im_init = self.mandelbrot()
        
        Writer = animation.writers['ffmpeg']
        writer = Writer(fps=15, metadata=dict(artist='Me'))

        fig = plt.figure()
        im = plt.imshow(im_init, cmap='bone')
        plt.axis('off')
        
        script_dir = os.path.dirname(__file__)
        results_dir = os.path.join(script_dir, 'Animations')
        sample_file_name = "Mandel_zoom"
        if not os.path.isdir(results_dir):
            os.makedirs(results_dir)
            
        def animate(i):
            im.set_data(Mandelbrot_disp(-1, -.3, 0.4-i/300,
                                        t_max=self.t_max, precision=self.precision).mandelbrot())
            return im,

        anim = animation.FuncAnimation(fig, animate, frames=150,interval=2, repeat=False,save_count=200)
        anim.save(os.path.join(results_dir, sample_file_name + 'test.avi'), writer=writer)
        plt.close()


    def mandel_loop(self):
        x, y = np.ogrid[self.x-self.facteur:self.x+self.facteur:(self.precision*1j),
                    self.y-self.facteur:self.y+self.facteur:(self.precision*1j)]
        c = x + 1j * y
        z=np.zeros(c.shape)
        mandel = np.zeros(c.shape)
        for i in range(50):
            z = z ** 2 + c
            mandel += 1 / float(2 + i) * (z * np.conj(z) > 4)
        return(mandel)
        
    def anim_pics_mandel(self):
        mlab.figure(size=(800, 800))
        mandel = self.mandel_loop()
        mlab.surf(mandel, colormap='hot', warp_scale='auto', vmax=1.5)
        script_dir = os.path.dirname(__file__)
        results_dir = os.path.join(script_dir, 'Animations')
        if not os.path.isdir(results_dir):
            os.makedirs(results_dir)
        for t in range(0,170,1):
            mlab.view(elevation=180-t)
            imgname = os.path.join(results_dir, 'rotation' + str(t) + ".png")
            mlab.savefig(imgname)
        for t in range(0,30,1):
            mlab.view(distance=1000-5*t, elevation=10)
            imgname = os.path.join(results_dir, 'rotation' + str(170+t) + ".png")
            mlab.savefig(imgname)
        mlab.close()
        os.system("ffmpeg -r 20 -i " + os.path.join(results_dir, "rotation") +
                    "%1d.png -vcodec mpeg4 -q:v 3 -ab 192k -y "+os.path.join(results_dir,"movie.avi"))

def mandel_branch_points(x0, mu, nb_iter=20):
    points = [(x0, 0)]
    for _ in range(nb_iter):
        f_x0 = x0**2+mu
        points.append((x0, f_x0))
        points.append((f_x0, f_x0))
        x0 = f_x0
    return points   