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
from zojax.richtext.field import RichTextProperty
"""

$Id$
"""
from zope import interface, component
from zope.size import byteDisplay
from zope.size.interfaces import ISized
from zope.proxy import removeAllProxies
from zope.lifecycleevent.interfaces import IObjectModifiedEvent

from zojax.content.type.container import ContentContainer

from interfaces import IUserManualPage


class UserManualPage(ContentContainer):
    interface.implements(IUserManualPage)

    body = RichTextProperty(IUserManualPage['body'])
