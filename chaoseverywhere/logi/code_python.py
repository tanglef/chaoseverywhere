import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
import matplotlib.gridspec as gridspec
from matplotlib import colors as mcolors
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

from ..mandel.create_mandel import Mandelbrot_disp, mandel_branch_points

def logistic(r, x):
    return(r*x*(1-x))


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
    plt.show()


def bifurcation(show=True):
    r = np.linspace(1, 4, 10000)
    x = []
    y = []
    for i in r:
        x.append(i)
        x0 = np.random.random()
        for _ in range(1000):
            x0 = logistic(i, x0)
        y.append(x0)
    
    if show:
        plt.plot(x, y, ls='', marker=',', color='blue')
        plt.show()
    else: return(x,y)

def logi_branch_points(x0, mu, nb_iter=100):
    points = [(x0,0)]
    for _ in range(nb_iter):
        f_x0 = logistic(mu,x0)
        points.append((x0,f_x0))
        points.append((f_x0,f_x0))
        x0 = f_x0
    return points

def plot_logi_interact(x0,mu,nb_iter=100,linsdim=100):
    """ Another way to plot the logistic function which is faster so more pleasant to use with the interaction."""
    x,y=zip(*logi_branch_points(x0, mu, nb_iter))
    vals = np.linspace(0,1,linsdim)
    plt.figure()
    plt.plot(vals,vals)
    plt.plot(vals, logistic(mu,vals))
    plt.plot(x,y,'k',color='red', alpha=.3)
    plt.show()

def animate_logistic(save=False):
    fig, ax = plt.subplots()  # initialise la figure
    line, = plt.plot([], [],color='red', alpha=.4)
    courbe, = plt.plot([], [], color='black')
    x = np.linspace(0, 1, 100)
    plt.plot(x, x)
    plt.suptitle("Evolution of the logistic map")

    def init():
        line.set_data([], [])
        courbe.set_data([],[])
        return line,

    def animate(i):
        line.set_data(zip(*logi_branch_points(.01, 1.015+i*0.015)))
        courbe.set_data(x, logistic(1.015+i*.015,x))
        ax.set_title(u"mu = {0:.3f}".format(1.015+i*0.015))
        return line, courbe, 

    ani = animation.FuncAnimation(
        fig, animate, init_func=init, frames=200, blit=True, interval=20, repeat=False)
    
    if save:
        script_dir = os.path.dirname(__file__)
        results_dir = os.path.join(script_dir, 'temp')
        if not os.path.isdir(results_dir):
            os.makedirs(results_dir)
        ani.save(os.path.join(results_dir, 'Chaos_in_logistic_map.mp4'))
    else: return(ani)

def connections():
    fig=plt.figure()
    plt.style.use(['ggplot', 'dark_background'])
    gs = gridspec.GridSpec(2, 4)

    ax1 = plt.subplot(gs[0, :2], )
    backgrd = Mandelbrot_disp(-.5, 0, 1, precision=400, t_max=100).mandelbrot()
    ax1.imshow(backgrd, cmap='bone_r', origin="lower")
    xl, = ax1.plot([],[],color='red')
    ax1.axhline(y=200, color='red')  # x=350 => x_m=.25
    x_coord = [350, 300, 200, 100, 0]
    y_coord = [200]*5
    to_disp = ['0.25', '0', '-0.5', '-1', '-1.5']
    for i, to_disp in enumerate(to_disp):
        x = x_coord[i]
        y = y_coord[i]
        ax1.scatter(x, y, color='magenta', marker='o')
        ax1.text(x+5, y+10, to_disp, fontsize=9, color='magenta')
    ax1.axis('off')

    ax2 = plt.subplot(gs[0, 2:])
    line, = ax2.plot([], [], color='red', alpha=1, lw=4)
    courbe, = ax2.plot([], [], color='dodgerblue', alpha=1, lw=2)
    x = np.linspace(-2, 1, 400)
    ax2.plot(x, x, color='green')

    ax3 = plt.subplot(gs[1, 1:3])
    x_vals, y_vals = bifurcation(show=False)
    ax3.plot(x_vals, y_vals, ls='', marker=',', color='white')
    xl3, = ax3.plot([],[],color='red')
    ax3.axis('off')

    fig.suptitle('Connection between the Mandelbrot set and \n the bifurcation diagram', size=10)

    def init():
        line.set_data([], [])
        xl.set_data([], [])
        courbe.set_data([], [])
        xl3.set_data([],[])
        return line, xl, courbe,

    def animate(i):
        line.set_data(zip(*mandel_branch_points(.01, 0.3-0.01*i)))
        courbe.set_data(x, x**2+(0.3-0.01*i))
        xl.set_data((.3-0.01*i)*200+300, [0,400])
        xl3.set_data(1.3+.015*i,[0,1])
        return courbe, xl,

    script_dir = os.path.dirname(__file__)
    results_dir = os.path.join(script_dir, 'temp')
    if not os.path.isdir(results_dir):
        os.makedirs(results_dir)

    ani_three = animation.FuncAnimation(
        fig, animate, init_func=init, frames=180, interval=20, repeat=False) 
    FFwriter = animation.FFMpegWriter(fps=10)     
    ani_three.save(os.path.join(results_dir, 'les_3.avi'), writer = FFwriter, dpi=300)