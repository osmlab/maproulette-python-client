import codecs
import os.path
from setuptools import setup, find_packages

with open("README.md", "r") as readme:
    long_description = readme.read()


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


name = "maproulette"
version = get_version(f"{name}/__init__.py")
setup(name=name,
      version=version,
      description="A Python API wrapper for MapRoulette",
      license="Apache License 2.0",
      long_description_content_type='text/markdown',
      long_description=long_description,
      url="https://github.com/osmlab/maproulette-python-client",
      packages=find_packages(exclude=["tests", "examples"]),
      python_requires='>=3.6',
      setup_requires=["pytest-runner"],
      tests_require=["pytest", "requests"],
      install_requires=["requests"])
