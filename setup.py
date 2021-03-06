# Upload package to PyPi.

from setuptools import setup

setup(name='tbapy',
      version='0.1.1',
      description='Unofficial Python library to get data from The Blue Alliance.',
      url='https://github.com/frc1418/tbapy',
      author='FRC Team 1418, Erik Boesen',
      author_email='robotics1418@gmail.com',
      license='MIT',
      packages=['tbapy'],
      install_requires=['requests'],
      zip_safe=False)
