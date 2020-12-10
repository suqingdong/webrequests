# -*- encoding: utf8 -*-
import os
import json
from setuptools import setup, find_packages


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

version_info = json.load(open(os.path.join(BASE_DIR, 'webrequests', 'version.json')))

print(version_info)

setup(
    name='webrequests',
    version=version_info['version'],
    author=version_info['author'],
    author_email=version_info['author_email'],
    description=version_info['desc'],
    long_description=open(os.path.join(BASE_DIR, 'README.md')).read(),
    long_description_content_type="text/markdown",
    url='https://github.com/suqingdong/webrequests',
    project_urls={
        'Tracker': 'https://github.com/suqingdong/webrequests/issues',
    },
    license='BSD License',
    install_requires=open(os.path.join(BASE_DIR, 'requirements.txt')).read().strip().split('\n'),
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ]
)
