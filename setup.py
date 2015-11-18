#!/usr/bin/env python
"""enplot: a one-line command line plotting tool for CSV data

enplot is a simple plotting tool for quickly visualizing data in CSV and
related formats. It uses Python/Scipy/matplotlib as backend.
"""
import os
from setuptools import setup


DOCLINES = __doc__.split('\n')
CLASSIFIERS = """\
Programming Language :: Python
Topic :: Engineering
Operating System :: POSIX
Operating System :: Unix
"""
NAME = "enplot"
MAJOR = 1
MINOR = 0
MICRO = 2
ISRELEASED = False
VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)
REVISION = 0 + int(os.popen("git rev-list --all | wc -l").read())


def write_version_py(filename=NAME+'/version.py'):
    if os.path.exists(filename):
        os.remove(filename)
    cnt = """\
# THIS FILE IS AUTOMATICALLY GENERATED BY ENPLOT SETUP.PY
version = '%(version)s'
revision = %(revision)s
release = %(isrelease)s
"""
    a = open(filename, 'w')
    try:
        a.write(cnt % {'version': VERSION,
                       'revision': REVISION,
                       'isrelease': str(ISRELEASED)})
    finally:
        a.close()

write_version_py()

setup(
    name=NAME,
    version=VERSION,
    packages=['enplot'],
    author="Robert Johansson",
    author_email="jrjohansson@gmail.com",
    license="LGPL",
    description=DOCLINES[0],
    long_description="\n".join(DOCLINES[2:]),
    keywords="plotting, one-line, command-line",
    url="http://github.com/jrjohansson",
    platforms=["Linux", "Unix"],
    package_data={'enplot': ['*.png'], },
    entry_points={
        'console_scripts': [
            'enplot = enplot.run:main'
        ]
    }
)
