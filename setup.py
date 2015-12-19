from setuptools import setup, find_packages
import sys, os

version = '0.0.1'

setup(name='clipmon',
      version=version,
      description="Watch your clipboard for path/line-number combos.  Open them in your editor.",
      long_description="""""",
      classifiers=[],
      keywords='clipboard monitor utility',
      author='Jesse Aldridge',
      author_email='JesseAldridge@gmail.com',
      url='https://github.com/JesseAldridge/clipmon',
      license='MIT',
      packages=['clipmon'],
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ]
      )
