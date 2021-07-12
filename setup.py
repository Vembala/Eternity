#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Sreerag M",
    author_email='sreeragibtl@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Eternity is my humble effort towards keeping an unbroken link with those whom I lost to dea",
    entry_points={
        'console_scripts': [
            'eternity=eternity.cli:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='eternity',
    name='eternity',
    packages=find_packages(include=['eternity', 'eternity.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/Sreerag-ibtl/eternity',
    version='0.1.0',
    zip_safe=False,
)
