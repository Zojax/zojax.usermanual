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
import rwproperty
from zope.component import getUtility
from zope.traversing.api import getParents
from zope.app.container.interfaces import INameChooser
from zojax.content.type.interfaces import IOrder, IDraftedContent, IContentType,\
    INameChooserConfiglet
from zojax.usermanual.interfaces import IUserManualPageType, IUserManual,\
    IUserManualPageDraft
from zojax.content.type.order import AnnotatableOrder, Reordable
from zojax.content.draft.interfaces import IDraftContent, DraftException,\
    IDraftPublishedEvent
from zojax.content.draft.draft import DraftContent
"""

$Id$
"""
from zope import interface, component, schema
from zope.size import byteDisplay
from zope.size.interfaces import ISized
from zope.proxy import removeAllProxies
from zope.lifecycleevent.interfaces import IObjectModifiedEvent
from zope.lifecycleevent import ObjectModifiedEvent

from zojax.content.draft.events import DraftPublishedEvent
from zojax.richtext.field import RichTextProperty
from zojax.content.type.container import ContentContainer
from interfaces import IUserManualPage, _


class UserManualPage(ContentContainer):
    interface.implements(IUserManualPage)

    text = RichTextProperty(IUserManualPage['text'])
    number = 1

    @rwproperty.getproperty
    def fullNumber(self):
        if IDraftedContent.providedBy(self):
            return self.__parent__.fullNumber
        if IUserManualPage.providedBy(self.__parent__):
            return '%s.%s'%(self.__parent__.fullNumber, self.number)
        return str(self.number)
    
    @rwproperty.setproperty
    def fullNumber(self, value):
        if IDraftedContent.providedBy(self):
            location = self.__parent__.getLocation()
            parents = filter(IUserManual.providedBy, [location] + getParents(location))
        else:
            parents = filter(IUserManual.providedBy, getParents(self))
        manual = parents[-1]
        numbers = map(int, value.split('.'))
        ct = getUtility(IContentType, name='content.usermanualpage')
        del self.__parent__[self.__name__]
        for number in numbers[0:-1]:
            try:
                manual = IOrder(manual).getByPosition(number)
            except KeyError:
                m = ct.create(_(u'Autocreated page'), _(u'Autocreated page description'))
                m.number = number
                ct.__bind__(manual).add(m)
                manual = m
        self.number = numbers[-1]
        manual[INameChooser(manual).chooseName(self.__name__, self)] = self
        IOrder(self.__parent__).rebuild()

        if IUserManualPage.providedBy(self.__parent__):
            return '%s.%s'%(self.__parent__.fullNumber, self.number)
        return str(self.number)
    
    @property
    def position(self):
        return IOrder(self.__parent__).keyPosition(self.__name__)
    
    @property
    def next(self):
        if IDraftedContent.providedBy(self):
            return None
        ob = self.__parent__.get(IOrder(self.__parent__).nextKey(self.__name__))
        if ob is not self:
            return ob
        elif len(self):
            return IOrder(self).values()[0]
    
    @property
    def previous(self):
        if IDraftedContent.providedBy(self):
            return None
        ob = self.__parent__.get(IOrder(self.__parent__).previousKey(self.__name__))
        if ob is not self:
            return ob
        
    @property
    def parent(self):
        if IUserManualPageType.providedBy(self.__parent__):
            return self.__parent__
        
        
class UserManualPageDraft(DraftContent):
    
    interface.implements(IUserManualPageDraft)
    
    def publish(self, comment=u''):
        content = super(UserManualPageDraft, self).publish(comment)
        content.fullNumber = self.fullNumber
        return content
    

class UserManualPageOrder(AnnotatableOrder):
    
    component.adapts(IUserManualPage)
    
    def generateKey(self, item):
        keys = self.order.keys()
        if item.number is None:
            item.number = 1
        while item.number in keys:
            item.number += 1
        return item.number