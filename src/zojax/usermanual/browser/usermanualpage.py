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
from zope.traversing.browser import absoluteURL

from zojax.layoutform import Fields
from zojax.filefield.field import FileField
from zojax.resourcepackage.library import include
from zojax.content.type.interfaces import IDraftedContent, IOrder
from zojax.content.browser.interfaces import IContainerListing
from zojax.table.column import Column
from zojax.table.interfaces import IDataset, ITableConfiguration
from zojax.content.browser import table

from zojax.usermanual.interfaces import _, IUserManualPage


class UserManualPageView(object):

    def update(self):
        include('zojax.usermanual')
        self.items = IOrder(self.context).values()
        

class FullNumberColumn(Column):
    component.adapts(IUserManualPage, interface.Interface, IContainerListing)

    name = 'fullNumber'
    title = _('Number')

    weight = 9

    def query(self, default=None):
        return self.content.fullNumber
    
    
class ContentsTableConfig(object):
    interface.implements(ITableConfiguration)

    disabledColumns = ()

    pageSize = 15

    enabledColumns = ('icon', 'fullNumber', 'name', 'title', 'created', 'modified')

    def __init__(self, context, request, table):
        self.context, self.request, self.table = context, request, table