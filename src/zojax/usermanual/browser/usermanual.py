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
from zojax.content.type.interfaces import IOrder
"""

$Id$
"""
from zope import interface
from zope.component import getUtility
from zope.traversing.browser import absoluteURL

from zojax.resourcepackage.library import include
from zojax.resourcepackage.library import includeInplaceSource

from zojax.usermanual.interfaces import _, IUserManualPage
from zojax.usermanual.interfaces import IUserManual, IUserManualProduct

from interfaces import IUserManualPageView


class UserManualView(object):
    interface.implements(IUserManualPageView)

    items = []

    def update(self):
        include('zojax.usermanual')

        product = getUtility(IUserManualProduct)

        self.url = absoluteURL(self.context, self.request)
        self.items = IOrder(self.context).values()


class UserManualModalView(UserManualView):
    """ class for modal view
    """

    def render(self):

        includeInplaceSource(jssource, ('jquery-treeview',))

        return super(UserManualModalView, self).render()



jssource = """<script type="text/javascript">
$(function() {
    $("#tree").treeview({
        collapsed: true,
        animated: "medium",
        persist: "location"
    });
})
</script>"""
