import chaoseverywhere as chaos

from mayavi import mlab
import numpy as np
#chaos.Mandelbrot_disp(-.5, 0, 1).disp_mandel()
#chaos.Mandelbrot_disp(-.5, 0, 1, t_max = 50, precision = 350).animate_mandel_plt()
#print(chaos.logistic(3.6, 0.001))

#chaos.Mandelbrot_disp(-.5,0,1.5).anim_pics_mandel(go_up=False)
#print(chaos.logistic_draw(.01,3,50,200))
#chaos.animate_logistic(save=True)
#chaos.connections()
#chaos.Mandelbrot_disp(0,0,2,t_max=150, precision=500).anim_puiss_mandel(remove=True)
def transform(z,c):
    return(((z ** 2 + c -1)/(2*z +c-2))**2)

#mandel = chaos.Mandelbrot_disp(1.5,0,2.5).mandel_transform(FUN=transform)

#mlab.figure(size=(800, 800))
#mlab.surf(mandel, colormap='hot', warp_scale='auto', vmax=1.5)
#mlab.view(elevation=180)
#mlab.savefig('3d_transform.png')
#mlab.show()


mandel = chaos.Mandelbrot_disp(-.5,0,1.5).tests()


mandel[np.isinf(mandel)]= np.nan
mlab.figure(size=(800, 800))
mlab.surf(mandel.real, mandel.imag, colormap='hot', warp_scale='auto', vmax=1.5)
mlab.view(elevation=180)
mlab.savefig('3d_transform.png')
mlab.show()


# base pattern is the mandelbrot set
# show the real part of the iterates on the vertical axis