import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-admin-watchdog',
    version='1.0.3',
    packages=find_packages(),
    include_package_data=True,
    license='GPLv3+',
    description='A simple Django app to register logs in admin backoffice.',
    long_description=README,
    url='https://github.com/makinacorpus/django-admin-watchdog',
    author='Yann Fouillat',
    author_email='yann.fouillat@makina-corpus.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
