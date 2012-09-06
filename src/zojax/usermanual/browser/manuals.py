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

from zope.component import queryMultiAdapter
from zope.dublincore.interfaces import IDCTimes
from zope.security.proxy import removeSecurityProxy
from zope.traversing.browser import absoluteURL

from zojax.batching.batch import Batch

from zojax.usermanual.interfaces import IUserManual


class UserManualsWorkspaceView(object):

    def update(self):
        context = self.context
        request = self.request

        data = []
        for item in context.values():
            if not IUserManual.providedBy(item):
                continue

            item = removeSecurityProxy(item)
            dc = IDCTimes(item)

            info = {'title': item.title,
                    'icon': queryMultiAdapter((item, request), name='zmi_icon'),
                    'url': absoluteURL(item, request),
                    'created': dc.created,
                    'modified': dc.modified,}

            data.append((item.title, info))

        data.sort()
        results = [info for t, info in data]

        self.batch = Batch(
            results, size = 10, prefix='manuals',
            context = context, request = request)

