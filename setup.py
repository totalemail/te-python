#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('LICENSE') as license_file:
    license = license_file.read()

requirements = [
    'click',
    'requests'
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='te_python',
    version='0.1.0',
    description="Python SDK for TotalEmail.",
    long_description=readme,
    author="Floyd Hightower",
    author_email='floyd.hightower27@gmail.com',
    url='https://gitlab.com/totalemail/te-python',
    packages=find_packages(exclude=('tests', 'docs')),
    # entry_points={
    #     'console_scripts': [
    #         'te_python=te_python.cli:main'
    #     ]
    # },
    include_package_data=True,
    install_requires=requirements,
    license=license,
    zip_safe=True,
    keywords='te_python',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
)
