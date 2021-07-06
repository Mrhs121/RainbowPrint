#!/usr/bin/env python
# coding: utf-8

# from setuptools import setup
import setuptools
filepath = 'README.md'
setuptools.setup(
    name='RainbowPrint',
    version='2.0.4',
    author='hs',
    author_email='huangshengtx@163.com',
    description=u'在终端中输出彩色文本',
    long_description=open(filepath, encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    install_requires=[],
)
