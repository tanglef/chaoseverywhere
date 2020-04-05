import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + (os.path.sep + '..'))

result_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "profile_time.prof")
find_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "snake_profile.py")

os.system("python -m cProfile -o " + result_dir + " " + find_dir)
os.system('snakeviz ' + result_dir)

os.system('mprof run memory_profile.py')
os.system('mprof plot --flame')