import numpy as np
import ffmpeg
import matplotlib.pyplot as plt
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
                           np.linspace(y-facteur, y+facteur, precision))
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

    def animate_mandel_plt(self, openvid=True):
        im_init = self.mandelbrot()
        
        Writer = animation.writers['ffmpeg']
        writer = Writer(fps=15, metadata=dict(artist='Me'))

        fig = plt.figure()
        im = plt.imshow(im_init, cmap='bone')
        plt.axis('off')
        
        script_dir = os.path.dirname(__file__) #only dans un py
        results_dir = os.path.join(script_dir, 'Animations/')
        sample_file_name = "Mandel_zoom"
        if not os.path.isdir(results_dir):
            os.makedirs(results_dir)
            
        def animate(i):
            im.set_data(Mandelbrot_disp(-1, -.3, 0.4-i/300,
                                        t_max=self.t_max, precision=self.precision).mandelbrot())
            return im,

        anim = animation.FuncAnimation(fig, animate, frames=150,interval=2, repeat=False,save_count=200)
        anim.save(results_dir + sample_file_name + 'test.avi', writer=writer)
        plt.close()
        if openvid:
            os.startfile(results_dir + sample_file_name + 'test.avi')
        else: return("You can find the animation at " + results_dir)
        