#! /usr/bin/env python

#    OpenDoor Web Directory Scanner
#    Copyright (C) 2017  Stanislav Menshov
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#    Development Team: Stanislav Menshov (Stanislav WEB)

from setuptools import setup, find_packages
import pypandoc
from src import Controller

try:
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name='opendoor',
    version=Controller.local_version(),
    packages=find_packages(),
    url='https://github.com/stanislav-web/OpenDoor',
    license='GPL',
    test_suite='tests',
    author='Stanislav Menshov',
    author_email='stanisov@gmail.com',
    description='OWASP Directory Access scanner',
    long_description=long_description,
    keywords=['owasp scanner', 'directory scanner', 'access directory scanner', 'web spider', 'auth scanner', 'dir search'],
    entry_points={
        'console_scripts': [
            'coveralls = coveralls.cli:main',
        ],
    },
    scripts=['opendoor.py'],
    install_requires=[line.rstrip('\n') for line in open('requirements.txt')],

    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Site Management :: Link Checking'
        'Topic :: Software Development :: src :: Python Modules',
    ],
)
