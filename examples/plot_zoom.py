"""
Title
=================
"""

################################
# Some Setup
# -------------------


import chaoseverywhere as chaos
import matplotlib.pyplot as plt
import os
import matplotlib.animation as animation
# sphinx_gallery_thumbnail_path = '../doc/_build/html/_images/thumbnail.svg'

im_init = chaos.Mandelbrot_disp(-.5,0,1.5)
im_init = im_init.mandelbrot()

Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'))

fig = plt.figure()
im = plt.imshow(im_init, cmap='bone')
plt.axis('off')

results_dir = '../doc/_build/html/_images/'
sample_file_name = "Mandel_zoom"
os.makedirs(results_dir, exist_ok=True)

def animate(i):
    im.set_data(chaos.Mandelbrot_disp(-1, -.3, 0.4-i/300,
            t_max=100,
            precision=400).mandelbrot())
    if(i==130):
        plt.savefig(results_dir + 'thumbnail.svg')
    return im,


anim = animation.FuncAnimation(fig, animate, frames=150, interval=2,
                                       repeat=False, save_count=200)
anim.save(results_dir + sample_file_name + '.mp4', writer=writer)

plt.close()



########################
# Else
# ----------------
# .. raw:: html
#
#          <video controls src="../../../_build/html/_images/Mandel_zoom.mp4"></video>

