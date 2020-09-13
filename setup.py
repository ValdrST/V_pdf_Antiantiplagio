#!/usr/bin/env python
# Stupid shit happened in pip 10: https://stackoverflow.com/a/49867265/965332
try:  # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements
from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

requirements = parse_requirements("./requirements.txt", session=False)

setup(name='vPdfAntiAntiPlagio',
      version="0.5.5",
      description='Aplicacion anti anti plagio',
      long_description=readme,
      long_description_content_type="text/markdown",
      author='Valdr Stiglitz',
      author_email='valdr.stiglitz@gmail.com',
      url='https://github.com/ValdrST/V_pdf_Antiantiplagio',
      packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
      include_package_data=True,
      install_requires=[i.strip() for i in open("./requirements.txt").readlines()],
      entry_points={
          'console_scripts': ['vPdfAntiAntiPlagio = vPdfAntiAntiPlagio:main','vPdfAntiAntiPlagioWSGI = vPdfAntiAntiPlagio:wsgi']
      },
      classifiers=[
          'Programming Language :: Python :: 3',
          "Operating System :: OS Independent",
      ])
