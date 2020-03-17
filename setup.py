from setuptools import setup
from chaoseverywhere import __version__ as current_version

setup(
  name='chaoseverywhere',
  version=current_version,
  description='Visualization of the Mandelbrot set and the logistic map',
  url='http://github.com/tanglef/chaoseverywhere.git',
  author='Ophelie Coiffier ; Tanguy Lefort ; Ibrahim Gaizi',
  author_email='tanguy.lefort@etu.umontpellier.fr',
  license='MIT',
  packages=['chaoseverywhere', 'chaoseverywhere.mandel'],
  zip_safe=False
)