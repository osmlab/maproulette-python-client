from setuptools import setup, find_packages
from maproulette import __version__

with open("README.md", "r") as readme:
    long_description = readme.read()

name = "maproulette"
version = __version__
setup(name=name,
      version=version,
      description="A Python API wrapper for MapRoulette",
      license="Apache License 2.0",
      long_description=long_description,
      url="https://github.com/osmlab/maproulette-python-client",
      packages=find_packages(exclude=["tests", "examples"]),
      python_requires='>=3.6',
      setup_requires=["pytest-runner"],
      tests_require=["pytest", "requests"],
      install_requires=["requests"])
