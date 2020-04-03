from setuptools import setup, find_packages

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(name="maproulette",
      version="1.0.0-alpha.1",
      description="A Python API wrapper for MapRoulette",
      long_description=long_description,
      url="https://github.com/osmlab/maproulette-python-client",
      packages=find_packages('maproulette'),
      python_requires='>=3.6',
      setup_requires=["pytest-runner"],
      tests_require=["pytest"],
      package_dir={'': 'maproulette'},
      install_requires=['requests'])
