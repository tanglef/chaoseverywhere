import os.path
import sys
import numpy as np
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + (os.path.sep + '..')*2)

import chaoseverywhere as chaos


def test_mandel():
    test = chaos.Mandelbrot_disp(-.5, 0, 1,t_max=10,precision=20).mandelbrot()
    assert test[0,0] == True

def test_logi():
    test = chaos.logistic(3.6, 0.001)
    assert np.isclose(0.0035964,test)

def test_mandel_loop():
    test = chaos.Mandelbrot_disp(-.5, 0, 1).mandel_loop()[0,0]
    assert np.isclose(test,1.5198773448773448)

def test_mandel_branch_points():
    assert np.allclose(chaos.mandel_branch_points(.01,.1)[1], [0.01, 0.10010000000000001])

def test_bifurcation():
    assert np.isclose(chaos.bifurcation(show=False)[0][18], 1.0054005400540054)