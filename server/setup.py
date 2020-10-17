from os import path
from setuptools import setup, find_packages


about = {}
here = path.abspath(path.dirname(__file__))
with open(path.join(here, '__version__.py'), 'r', encoding='utf-8') as f:
  exec(f.read(), about)

with open('README.md', 'r', encoding='utf-8') as f:
  readme = f.read()

print(about)

setup(
  name='flask-app',#about['__title__'],
  version='1.0.0',#about['__version__'],
  packages=find_packages(where='app'),
  package_dir={'': 'app'},
  install_requires=['flask'],
  extras_require={'test': ['pytest', 'pytest-cov']},
)

"""


setup(


  author=about['__author__'],
  author_email=about['__author_email__'],
  packages=find_packages(where='app'),

  extras_require={'test': ['pytest', 'pytest-cov']},
)
"""
