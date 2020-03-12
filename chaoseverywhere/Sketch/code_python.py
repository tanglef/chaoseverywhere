import numpy as np
import matplotlib.pyplot as plt


def logistic(r, x):
    return(r*x*(1-x))


def logistic_draw(x0, r, iteration, points):
    """ This function is able to draw the logistic function, the curve (y=x)
    and the intersections beetwen these two curves recursively.
    """
    x = np.linspace(0, 1, points)
    plt.figure()
    plt.plot(x, logistic(r, x))
    plt.plot(x, x)
    for i in range(iteration):
        f_x0 = logistic(r, x0)
        plt.plot([x0, x0], [x0, f_x0],
                 color='red', alpha=0.3)  # vertical stairs
        plt.plot([x0, f_x0], [f_x0, f_x0],
                 color='red', alpha=0.3)  # horizontal stairs
        plt.plot([x0, f_x0], [f_x0, f_x0], 'o',
                 color='grey', alpha=0.4)  # intersections
        x0 = f_x0
    plt.show()
        