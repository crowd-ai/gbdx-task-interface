import os
from os import path

from setuptools import setup, find_packages


VERSION = '1.0.3'


here = path.abspath(path.dirname(__file__))


def get_version():

    build_number = 0

    if os.path.exists('.buildinfo'):
        with open('.buildinfo') as f:
            build_number = f.readline()

    return VERSION + '.{}'.format(build_number)


# Get the long description from the relevant file
setup(
    name='gbdx-task-interface',
    version=get_version(),
    packages=find_packages(),
    description='A helper base class for easier GBDX application on-boarding.',
    url='https://github.com/tdg-platform',
    author='GBDX (Dmitry Zviagintsev)',
    author_email='dmitry.zviagintsev@digitialglobe.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
    package_data={
        'gbdx_task_interface': [],
    },
    include_package_data=True
)
