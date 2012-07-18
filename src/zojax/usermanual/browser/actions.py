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
from zope import interface, component
from zope.security import checkPermission
from zope.security.proxy import removeSecurityProxy
from zope.traversing.browser import absoluteURL
from zope.traversing.api import getParents

from zojax.usermanual.interfaces import _
from zojax.usermanual.interfaces import IUserManualPage, IUserManual, IUserManualsWorkspace
from zojax.content.actions.interfaces import \
    IAddContentCategory, IManageContentCategory
from zojax.content.actions.interfaces import IContextAction, IContentAction
from zojax.content.actions.contentactions import AddContent
from zojax.content.space.interfaces import IContentSpace
from zojax.personal.content.interfaces import IContentWorkspace

import interfaces


class BaseViewUserManualAction(object):
    component.adapts(IUserManualPage, interface.Interface)
    interface.implements(IContentAction, interfaces.IViewUserManualAction)

    weight = 300
    title = _(u'View manual')
    description = u''

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def url(self):
        return '%s/'%absoluteURL(filter(IUserManual.providedBy, getParents(self.context))[0], self.request)

    def isAvailable(self):
        return True


class ViewUserManualAction(BaseViewUserManualAction):
    interface.implements(IManageContentCategory)


class ContextViewUserManualAction(BaseViewUserManualAction):
    interface.implements(IContextAction)

    weight = 0


class UserManualRSSFeedAction(object):
    component.adapts(IUserManual, interface.Interface)
    interface.implements(interfaces.IUserManualRSSFeedAction)

    weight = 99999
    title = _(u'RSS Feed')
    description = u''

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def url(self):
        return '%s/@@feeds/usermanuals'%absoluteURL(self.context, self.request)

    def isAvailable(self):
        return True


class UserManualModalViewAction(object):
    component.adapts(IUserManual, interface.Interface)
    interface.implements(interfaces.IUserManualModalViewAction)

    weight = 5
    title = _(u'Modal View')
    description = u''
    target = '_blank'

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def url(self):
        return '%s/modal.html'%absoluteURL(self.context, self.request)

    def isAvailable(self):
        return True
