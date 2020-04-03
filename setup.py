from setuptools import setup, find_packages

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(name="maproulette",
      version="1.0.0-alpha.4",
      description="A Python API wrapper for MapRoulette",
      license="Apache License 2.0",
      long_description=long_description,
      url="https://github.com/osmlab/maproulette-python-client",
      packages=find_packages(exclude=["tests", "examples"]),
      python_requires='>=3.6',
      setup_requires=["pytest-runner"],
      tests_require=["pytest"],
      install_requires=['requests'])
