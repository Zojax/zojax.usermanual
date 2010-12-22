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
from zope import interface, schema
from zope.i18nmessageid import MessageFactory

from zojax.richtext.field import RichText
from zojax.content.type.interfaces import IItem
from zojax.content.feeds.interfaces import IRSS2Feed
from zojax.content.space.interfaces import IWorkspace, IWorkspaceFactory

_ = MessageFactory('zojax.usermanual')


class IUserManualItem(IItem):
    
    body = RichText(
        title = _(u'Body'))


class IUserManualPage(IUserManualItem):
    """ user manual page """
    
    number = interface.Attribute('number')
    
    position = interface.Attribute('position')
    
    next = interface.Attribute('next')
    
    previous = interface.Attribute('previous')
    
    parent = interface.Attribute('parent')
    

class IUserManualPageType(interface.Interface):
    """ user manual page content type """


class ISimpleUserManualPageType(interface.Interface):
    """ simple user manual page content type """


class IUserManual(IUserManualItem):
    """ user manual """


class IUserManualType(interface.Interface):
    """ user manual content type """


class IUserManualProduct(interface.Interface):
    """ usermanual product """


class IUserManualsWorkspace(IItem, IWorkspace):
    """ user manuals workspace """


class IUserManualsWorkspaceFactory(IWorkspaceFactory):
    """ user manuals workspace factory """


class IUserManualsRSSFeed(IRSS2Feed):
    """ user manuals rss feed """
