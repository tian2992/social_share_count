#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Flask','python-twitter','gunicorn', 'flask-cors', 'psycopg2', 'sqlalchemy', 'flask-caching']

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Sebastian Oliva",
    author_email='code@sebastianoliva.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Track tuiter shares.",
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='social_share_count',
    name='social_share_count',
    packages=find_packages(include=['social_share_count']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/tian2992/social_share_count',
    version='0.1.0',
    zip_safe=False,
)
