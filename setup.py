from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='apiconsumer',
    version='1.0.0b1',
    description='Lightweight requests wrapper for REST API calls',
    long_description=long_description,
    url='https://github.com/saberr/apiconsumer',
    author='Marko Stanojkovic',
    author_email='marko@saberr.com',
    license='BSD 3-Clause',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=['apiconsumer'],
    install_requires=['requests>=2.18.4'],
    tests_require=['responses>=0.8.1', 'nose'],
    test_suite='nose.collector',
)
