__author__ = 'ziyasal'

from setuptools import setup

setup(
    name='socket.io-emitter',
    version='0.1.0',
    author='Ziya SARIKAYA',
    author_email='sarikayaziya@gmail.com',
    packages=['emitter'],
    scripts=['emitter/emitter.py'],
    url='https://github.com/ziyasal/socket.io-python-emitter',
    license='LICENSE',
    description='A Python implementation of socket.io-emitter',
    long_description=open('README.md').read(),
    install_requires=['msgpack-python', 'redis']
)
