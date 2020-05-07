import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + (os.path.sep + '..'))

import chaoseverywhere as chaos

chaos.connections()

results_dir = os.path.join(os.path.dirname(__file__), "img_connections")
if not os.path.isdir(results_dir):
    os.makedirs(results_dir)

dir_video = os.path.join(os.path.dirname(__file__), "..", "chaoseverywhere", "logi", "temp", "les_3.avi")
os.system("ffmpeg -i " + dir_video + " -r 20 -f image2 " + os.path.join(results_dir, "les_3-") + "%d.pdf")