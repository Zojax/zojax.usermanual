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
import re
from string import capitalize

from zope import interface, schema
from zope.i18nmessageid import MessageFactory
from zope.schema._bootstrapinterfaces import ConstraintNotSatisfied

from zojax.content.draft.interfaces import IDraftContent
from zojax.richtext.field import RichText
from zojax.content.type.interfaces import IItem
from zojax.content.feeds.interfaces import IRSS2Feed
from zojax.content.space.interfaces import IWorkspace, IWorkspaceFactory

_ = MessageFactory('zojax.usermanual')


class FullNumberValidationError(ConstraintNotSatisfied) :
    """ Error in regexp matching """

    def doc(self):
        return capitalize(", ".join(self.args))
    
FULL_NUMBER_CONDITION_PARAMS = (
        (True, re.compile(r"^(\d+\.?)+$").match, _(u"Full number must be period-separated numbers like 1.2.3")),
        )

def FULL_NUMBER_CONDITION(value):
    res = []
    for flag, rex, title in FULL_NUMBER_CONDITION_PARAMS:
        if not (flag == bool(rex(value))):
            res.append(title)
    if res:
        raise FullNumberValidationError(*res)
    return True


class IUserManualItem(IItem):
    
    text = RichText(
        title = _(u'Text'),
        required = False)


class IUserManualPage(IUserManualItem):
    """ user manual page """
    
    number = interface.Attribute('number')
    
    fullNumber = schema.TextLine(title=_(u'Full Page number'),
                        description=_(u'Period-separated. Defers page position. If parent pages are not existent, they will be autocreated'),
                        constraint=FULL_NUMBER_CONDITION
                        )
    
    position = interface.Attribute('position')
    
    next = interface.Attribute('next')
    
    previous = interface.Attribute('previous')
    
    parent = interface.Attribute('parent')
    
    
class IUserManualPageDraft(interface.Interface):
    
    fullNumber = schema.TextLine(title=_(u'Full Page number'),
                        description=_(u'Period-separated. Defers page position. If parent pages are not existent, they will be autocreated'),
                        constraint=FULL_NUMBER_CONDITION
                        )
    

class IUserManualPageType(interface.Interface):
    """ user manual page content type """


class ISimpleUserManualPageType(interface.Interface):
    """ simple user manual page content type """


class IUserManual(IItem):
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
