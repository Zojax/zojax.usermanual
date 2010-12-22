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
from zope.traversing.api import getParents
from zojax.content.type.interfaces import IOrder
from zojax.usermanual.interfaces import IUserManualPageType
"""

$Id$
"""
from zope import interface, component
from zope.size import byteDisplay
from zope.size.interfaces import ISized
from zope.proxy import removeAllProxies
from zope.lifecycleevent.interfaces import IObjectModifiedEvent

from zojax.richtext.field import RichTextProperty
from zojax.content.type.container import ContentContainer

from interfaces import IUserManualPage


class UserManualPage(ContentContainer):
    interface.implements(IUserManualPage)

    body = RichTextProperty(IUserManualPage['body'])

    @property
    def number(self):
        if IUserManualPage.providedBy(self.__parent__):
            return '%s.%s'%(self.__parent__.number, self.position)
        return str(self.position)
    
    @property
    def position(self):
        return IOrder(self.__parent__).keyPosition(self.__name__)
    
    @property
    def next(self):
        ob = self.__parent__.get(IOrder(self.__parent__).nextKey(self.__name__))
        if ob is not self:
            return ob
        elif len(self):
            return IOrder(self).values()[0]
    
    @property
    def previous(self):
        ob = self.__parent__.get(IOrder(self.__parent__).previousKey(self.__name__))
        if ob is not self:
            return ob
        
    @property
    def parent(self):
        if IUserManualPageType.providedBy(self.__parent__):
            return self.__parent__