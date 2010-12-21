##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
""" Setup for zojax.usermanual package

$Id$
"""
import sys, os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version='1.3.8dev'


setup(name = 'zojax.usermanual',
      version = version,
      author = 'Anatoly Bubenkov',
      author_email = 'bubenkoff@gmail.com',
      description = "User Manual Tool for zojax.",
      long_description = (
          'Detailed Documentation\n' +
          '======================\n'
          + '\n\n' +
          read('CHANGES.txt')
          ),
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Framework :: Zope3'],
      url='http://zojax.net/',
      license='ZPL 2.1',
      packages=find_packages('src'),
      package_dir = {'':'src'},
      namespace_packages=['zojax'],
      install_requires = ['setuptools', 'rwproperty', 'ZODB3',
                          'zope.schema',
                          'zope.component',
                          'zope.interface',
                          'zope.security',
                          'zope.publisher',
                          'zope.i18n',
                          'zope.i18nmessageid',
                          'zope.app.component',
                          'zope.app.security',
                          'zope.app.pagetemplate',
                          'z3c.traverser',
                          'zojax.batching',
                          'zojax.layout',
                          'zojax.layoutform',
                          'zojax.content.type',
                          'zojax.content.feeds',
                          'zojax.content.forms',
                          'zojax.content.draft',
                          'zojax.content.space',
                          'zojax.content.permissions',
                          'zojax.personal.space',
                          'zojax.personal.content',
                          'zojax.product',
                          'zojax.statusmessage',
                          'zojax.richtext'
                          ],
      extras_require = dict(test=['zope.app.testing',
                                  'zope.testing',
                                  'zope.testbrowser',
                                  'zojax.content.browser [test]',
                                  ]),
      include_package_data = True,
      zip_safe = False
      )
