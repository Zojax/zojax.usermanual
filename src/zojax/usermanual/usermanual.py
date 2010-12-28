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
from BTrees.Length import Length
from BTrees.OOBTree import OOTreeSet

from zope import interface, component
from zope.schema.fieldproperty import FieldProperty
from zope.security.proxy import removeSecurityProxy
from zope.app.container.interfaces import IObjectAddedEvent
from zope.app.container.interfaces import IObjectRemovedEvent

from zojax.content.type.container import ContentContainer
from zojax.richtext.field import RichTextProperty

from interfaces import IUserManual


class UserManual(ContentContainer):
    interface.implements(IUserManual)
    