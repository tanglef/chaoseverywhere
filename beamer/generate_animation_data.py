import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + (os.path.sep + '..'))

import chaoseverywhere as chaos

chaos.connections()

dir_video = os.path.join(os.path.dirname(__file__), "..", "chaoseverywhere", "logi", "temp", "les_3.avi")
result_dir = os.path.dirname(__file__)
os.system("ffmpeg -i " + dir_video + " -r 20 -f image2 " + os.path.join(result_dir, "les_3-") + "%d.pdf")