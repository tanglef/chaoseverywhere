import numpy as np
import matplotlib.pyplot as plt
from mayavi import mlab
import matplotlib.animation as animation
import os
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)


class Mandelbrot_disp:
    """This class creates the mandlebrot graph and zooms in on this graph.
    Moreover, there are functions who display the Mandlebrot set in 2D and 3D with animated video.

    :param x: coordinate of the image's center
    :type x: float
    :param y: coordinate on the Imaginary axis
    :type y: float
    :param facteur: the remoteness of the image's center
    :type facteur: float
    :param t_max: the iteration's number of the sequence (zn)
    :type t_max: integer
    :param precision: number of terms in the array (using to build the image)
    :type precision: integer
    """

    def __init__(self, x, y, facteur, t_max=100, precision=400):
        """Construction method.
        """
        self.x = x
        self.y = y
        self.facteur = facteur
        self.t_max = t_max
        self.precision = precision

    def mandelbrot(self):
        """This function gives a boolean matrix. 
        We affect the value True if the point is in the Mandlebrot set, false otherwise.

        :return: a matrix indicating whether or not the point is in Mandlebrot set.
        :rtype: numpy array
        """
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

    def disp_mandel(self):
        """Using the array of the mandlebrot function, this function shows the mandlebrot set.

        :return: plot the Mandlebrot set
        :rtype: matplotlib plot 
        """
        mandel = self.mandelbrot()
        plt.figure()
        plt.imshow(mandel, cmap='bone')  # interpolation induite
        plt.axis('off')
        plt.show()

    def animate_mandel_plt(self):
        """This function is able to zoom in on the Mandlebrot graph.
        This animation zooms in on the point (-1, -0.3) to see the fractals.

        :return: the animation of the Mandlebrot's zoom saved in .avi
        :rtype: matplotlib plot
        """
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
                                        t_max=self.t_max,
                                        precision=self.precision).mandelbrot())
            return im,

        anim = animation.FuncAnimation(fig, animate, frames=150, interval=2,
                                       repeat=False, save_count=200)
        anim.save(os.path.join(results_dir, sample_file_name + 'test.avi'),
                  writer=writer)
        plt.close()

    def mandel_loop(self, go_up=True, puiss=2):
        """This function determines coordinates of points, in the Mandlebrot set and the speed of divergence.

        :param go_up: type of display, condition to give values in mandel's array
        :type: boolean
        :param puiss: the exponant in the Mandlebrot equation
        :return: the Mandlebrot set in colors 
        :rtype: numpy array
        """
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

    def anim_pics_mandel(self, go_up=True, puiss=2):
        """This function shows the Mandlebrot set in 3D.
        It saves the video in .avi.

        :param go_up: type of display, using in mandle_loop function
        :type go_up: boolean
        :param puiss: the exponent in the Mandlebrot equation, using in the mandle_loop function
        :type puiss: integer
        """
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
        os.system("ffmpeg -r 20 -i " + os.path.join(results_dir, "rotation") +
                  "%1d.png -vcodec mpeg4 -q:v 3 -ab 192k -y " +
                  os.path.join(results_dir, "movie.avi"))

    def anim_puiss_mandel(self, remove=True):
        """ This function animates the Mandlebrot zoom.
        Actually, this function successively zooms in on the graph, on the bifurcations of the graph.
        We see the infinite repetition of the fractals, representing Mandlebrot set.

        :return: successive zoom of the Mandlebrot set
        :rtype: Animation / video
        """
        mlab.figure(size=(800, 800))
        mandel = self.mandel_loop(go_up=False)
        s = mlab.surf(mandel, colormap='hot', warp_scale='auto', vmax=1.5)
        script_dir = os.path.dirname(__file__)
        results_dir = os.path.join(script_dir, 'Animations')
        if not os.path.isdir(results_dir):
            os.makedirs(results_dir)

        for t in range(2, 100, 1):
            s.mlab_source.scalars = self.mandel_loop(go_up=False, puiss=t)
            imgname = os.path.join(results_dir, 'puiss' + str(t) + ".png")
            mlab.view(elevation=180)
            mlab.savefig(imgname)
        mlab.close()
        os.system("ffmpeg -r 5 -i " + os.path.join(results_dir, "puiss") +
                  "%1d.png -vcodec mpeg4 -q:v 3 -ab 192k -y " +
                  os.path.join(results_dir, "movie_puiss.avi"))
        if remove:
            folder = os.listdir(results_dir)
            for item in folder:
                if item.startswith("puiss"):
                    os.remove(os.path.join(results_dir, item))
        
    def mandel_transform(self, FUN):
        """This function determines coordinates of points in the transformation of the Mandelbrot set.

        :param FUN: function that replaces the mandelbrot recursive equation
        :type FUN: function
        :return: the Mandlebrot set transformed 
        :rtype: numpy array
        """
        x, y = np.ogrid[self.x - self.facteur:self.x +
                        self.facteur:(self.precision * 1j),
                        self.y - self.facteur:self.y +
                        self.facteur:(self.precision * 1j)]
        c = x + 1j * y
        z = np.zeros(c.shape)
        mandel = np.zeros(c.shape)
        for i in range(self.t_max):
            z = FUN(z,c)
            mandel += 1 / float(2 + i) * (z * np.conj(z) > 4)
        return(mandel)         


def mandel_branch_points(x0, mu, nb_iter=20):
    """ This function gives the coordinates of Mandlebrot points.
    Starting with the coordinate of (x0,0), the function applies the Mandlebrot sequence. Each coordinates
    is appended in a list, useful to draw stairs of the recursive sequence.

    :param x0: the starting point included in [0,1]
    :type x0: float
    :param mu: the common ratio of the Mandlebrot sequence, included in [0,1]
    :type mu: float
    :param nb_iter: the number of coordinates put in our final list
    :type nb_iter: integer
    :return: list of Mandlebrot points coordinates
    :rtype: list of tuples
    """
    points = [(x0, 0)]
    for _ in range(nb_iter):
        f_x0 = x0**2+mu
        points.append((x0, f_x0))
        points.append((f_x0, f_x0))
        x0 = f_x0
    return points
