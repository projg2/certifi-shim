#!/usr/bin/env python
# vim:fileencoding=utf-8:noet

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
