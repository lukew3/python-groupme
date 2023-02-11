from setuptools import setup, find_packages

setup(name='groupme',
      version='0.0.1',
      description='Python wrapper for the GroupMe API',
      url='https://github.com/lukew3/mathgenerator',
      author='Luke Weiler',
      author_email='lukew25073@gmail.com',
      license='GPLv3',
      install_requires=['requests'],
      packages=find_packages(),
)
