# -*- coding: utf-8 -*-
"""
/***************************************************************************
 VixedRequests
                                 A QGIS plugin
 Generate
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2019-10-21
        copyright            : (C) 2019 by mitkin
        email                : mikhail@npolar.no
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

__author__ = 'mitkin'
__date__ = '2019-10-21'
__copyright__ = '(C) 2019 by mitkin'


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load VixedRequests class from file VixedRequests.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .vixed_requests import VixedRequestsPlugin
    return VixedRequestsPlugin(iface)
