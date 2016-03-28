#!/usr/bin/env python3

from setuptools import setup

setup(
    name='cryptohelper',
    version='0.2.2',
    description='Helper functions to make using RSA+AES encryption with '
                'a redundantly split shared key more easy',
    author='Micha Gorelick',
    author_email='mynameisfiber@gmail.com',
    url='http://github.com/mynameisfiber/cryptohelper/',
    download_url='https://github.com/mynameisfiber/cryptohelper/tarball/master',
    license="MIT",

    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries",
        "Topic :: Security :: Cryptography",
    ],

    packages=['cryptohelper'],

    install_requires=[
        "pycrypto>=2.6.1",
        "secretsharing>=0.2.9",
    ],
    dependency_links=[
        "git+https://github.com/mynameisfiber/secret-sharing.git",
    ],
)

