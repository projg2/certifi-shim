#!/usr/bin/env python
# vim:fileencoding=utf-8:noet

# While I generally consider it an antipattern to try and support both
# setuptools and distutils with a single setup.py, in this specific instance
# where certifi is a dependency of setuptools, it can create a circular
# dependency when projects attempt to unbundle stuff from setuptools and pip.
# Though we don't really support that, it makes things easier if we do this and
# should hopefully cause less issues for end users.

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from certifi import __version__


setup(
    name='certifi',
    version=__version__,
    description='certifi-shim -- thin replacement for Python certifi '
                'package using system certificate store',
    author='Michał Górny',
    author_email='mgorny@gentoo.org',
    url='https://github.com/mgorny/certifi-shim',
    packages=[
        'certifi',
    ],
    license='CC0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Programming Language :: Python',
    ],
)
