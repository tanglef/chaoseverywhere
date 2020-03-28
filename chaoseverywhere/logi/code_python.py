import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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


def bifurcation():
    r = np.linspace(2.7, 4, 10000)
    x = []
    y = []
    for i in r:
        x.append(i)
        x0 = np.random.random()
        for _ in range(500):
            x0 = logistic(i, x0)
        y.append(x0)
    plt.plot(x, y, ls='', marker=',', color='blue')
    plt.show()

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

def animate_logistic():
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
    return(ani)