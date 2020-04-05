import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.system('mprof run memory_profile.py')
os.system('mprof plot --flame')