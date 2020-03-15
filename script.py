import chaoseverywhere as chaos

chaos.Mandelbrot_disp(-.5, 0, 1).disp_mandel()
chaos.Mandelbrot_disp(-.5, 0, 1, t_max = 50, precision = 350).animate_mandel_plt()
