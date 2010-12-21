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
from zope import interface, component, event
from zope.lifecycleevent import ObjectCreatedEvent
from zope.lifecycleevent import ObjectModifiedEvent
from zope.security.proxy import removeSecurityProxy
from zojax.content.space.interfaces import IContentSpace
from zojax.content.space.workspace import WorkspaceFactory
from zojax.content.type.container import ContentContainer

from interfaces import IUserManualsWorkspace, IUserManualsWorkspaceFactory


class UserManualsWorkspace(ContentContainer):
    interface.implements(IUserManualsWorkspace)

    @property
    def space(self):
        return self.__parent__


class UserManualsWorkspaceFactory(WorkspaceFactory):
    component.adapts(IContentSpace)
    interface.implements(IUserManualsWorkspaceFactory)

    name = 'usermanuals'
    title = _(u'User Manuals')
    description = _(u'Space user manuals workspace.')
    weight = 901
    factory = UserManualsWorkspace
