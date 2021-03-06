#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

import subprocess, os

def check_file(f):
    if not os.path.exists(f):
        print("Could not find {}".format(f))
        subprocess.run(['git submodule update --init --recursive'], cwd=cwd, shell=True)

cwd = os.path.dirname(os.path.abspath(__file__))
lib_path = os.path.join(cwd, "pymoskito/libs")
check_file(os.path.join(lib_path, "pybind11", "CMakeLists.txt"))

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read().replace(".. :changelog:", "")

with open("requirements.txt") as requirements_file:
    requirements = requirements_file.read()

test_requirements = [
]

setup(
    name="pymoskito",
    version="0.3.0",
    description="Python based modular simulation & postprocessing kickass "
                "toolbox",
    long_description=readme + "\n\n" + history,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="pymoskito control simulation feedback feedforward",
    url="https://github.com/cklb/pymoskito",
    author="Stefan Ecklebe",
    author_email="stefan.ecklebe@tu-dresden.de",
    license="GPLv3",
    packages=find_packages(),
    package_dir={"pymoskito": "pymoskito"},
    install_requires=requirements,
    include_package_data=True,
    test_suite="pymoskito.tests",
    tests_require=test_requirements,
    zip_safe=False
)
