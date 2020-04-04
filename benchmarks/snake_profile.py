import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + (os.path.sep + '..'))

import chaoseverywhere as chaos

chaos.Mandelbrot_disp(-.5,0,1, t_max=300).mandelbrot()
chaos.Mandelbrot_disp(-.5,0,1, t_max=300).mandel_loop()
chaos.bifurcation(show=False)

#cProfile.run('chaos.Mandelbrot_disp(-.5,0,1, t_max=300).mandelbrot()', os.path.join('.','mandel.prof'))
#cProfile.run('chaos.Mandelbrot_disp(-.5,0,1, t_max=300).mandel_loop()', 'mandel_loop.prof')
#cProfile.run('chaos.bifurcation(show=False)', 'bifurcation.prof')


