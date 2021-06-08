from setuptools import setup
from setuptools import find_packages

setup(
    name='dlgo',
    version='0.1',
    description='The-Game-of-Go-with-Deep-Learning',
    url='https://github.com/geegoo2015/The-Game-of-Go-with-Deep-Learning.git',
    install_requires=['tensorflow', 'keras', 'gomill', 'Flask>=0.10.1', 'Flask-Cors','future', 'h5py', 'six'],
    license='MIT',
    packages=find_packages(),
    zip_safe=False)