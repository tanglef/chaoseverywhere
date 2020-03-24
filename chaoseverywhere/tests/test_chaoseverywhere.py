import os.path
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + (os.path.sep + '..')*2)

import chaoseverywhere as chaos

def test_mandel():
    test = chaos.Mandelbrot_disp(-.5, 0, 1,t_max=10,precision=20).mandelbrot()
    assert test[0,0]==True

def test_logi():
    test = chaos.logistic(3.6, 0.001)
    assert test == 0.0035964
    