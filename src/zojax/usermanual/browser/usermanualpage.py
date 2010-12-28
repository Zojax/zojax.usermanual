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
from zojax.layoutform.subform import PageletEditSubForm
from zojax.content.forms.content import ContentBasicFields
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

from zojax.usermanual.interfaces import _, IUserManualPage, IUserManualPageType,\
    IUserManualPageDraft


class UserManualPageView(object):

    def update(self):
        include('zojax.usermanual')
        self.items = IOrder(self.context).values()
        

class NumberForm(PageletEditSubForm):

    @property
    def fields(self):
        if IDraftedContent.providedBy(self.context):
            return Fields(IUserManualPageDraft)
        return Fields()
    
    def getContent(self):
        if IDraftedContent.providedBy(self.context):
            return self.parentForm.wizard.draft

    def isAvailable(self):
        return IDraftedContent.providedBy(self.context)
    

class FullNumberColumn(Column):
    component.adapts(IUserManualPageType, interface.Interface, IContainerListing)

    name = 'fullNumber'
    title = _('Number')

    weight = 9

    def query(self, default=None):
        return self.content.fullNumber
    
    
class ContentBasicFields(ContentBasicFields):
    
    @property
    def fields(self):
        res = super(ContentBasicFields, self).fields
        if IDraftedContent.providedBy(self.context):
            res = res.omit('fullNumber')
        return res
    
    
class ContentsTableConfig(object):
    interface.implements(ITableConfiguration)

    disabledColumns = ()

    pageSize = 15

    enabledColumns = ('icon', 'fullNumber', 'name', 'title', 'created', 'modified')

    def __init__(self, context, request, table):
        self.context, self.request, self.table = context, request, table