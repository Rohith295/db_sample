from setuptools import setup
from wheel_proj import __version__

with open("requirements.txt") as f:
    requirements = f.read().split()

setup(name='wheel_proj',
      version=__version__,
      description='Python based test project',
      author='noone',
      author_email='noone',

      packages=['wheel_proj'],
      install_requires=requirements
      )
