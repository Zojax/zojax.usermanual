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
"""

$Id$
"""
from zope import interface
from zope.traversing.browser import absoluteURL

from zojax.layoutform import Fields
from zojax.filefield.field import FileField
from zojax.resourcepackage.library import include
from zojax.content.type.interfaces import IDraftedContent

from zojax.usermanual.interfaces import _, IUserManualPage


class UserManualPageView(object):

    def update(self):
        include('zojax.usermanual')