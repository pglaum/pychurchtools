import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="churchtools",
    version="0.1.13",
    author="Philipp Glaum",
    author_email="p@pglaum.de",
    description=("A library for the ChurchTools API"),
    license="GPLv3",
    keywords="api churchtools",
    url="https://git.sr.ht/~pglaum/pychurchtools",
    packages=["churchtools"],
    install_requires=["pydantic==1.10.10", "requests"],
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
