from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name="maproulette",
      version="0.0.1",
      description="A Python API wrapper for MapRoulette",
      long_description=long_description,
      url="https://github.com/osmlab/maproulette-python-client",
      packages=find_packages(),
      python_requires='>=3.6',
      setup_requires=["pytest-runner"],
      tests_require=["pytest"],
      package_dir={'': 'maproulette'},
      install_requires=['requests'])
