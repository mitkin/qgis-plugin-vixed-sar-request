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
"""

__author__ = 'mitkin'
__date__ = '2019-10-21'
__copyright__ = '(C) 2019 by mitkin'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

import os
import sys
import inspect

from qgis.PyQt.QtWidgets import QAction
from qgis.PyQt.QtGui import QIcon
import processing

from qgis.core import (QgsProcessingAlgorithm,
                       QgsApplication,
                       QgsProcessingParameterExtent,
                       QgsProcessingParameterFolderDestination)

from .vixed_requests_provider import VixedRequestsProvider

cmd_folder = os.path.split(inspect.getfile(inspect.currentframe()))[0]

if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


class VixedRequestsPlugin(object):

    def __init__(self, iface):
        self.provider = None
        self.iface = iface

    def initProcessing(self):
        """Init Processing provider for QGIS >= 3.8."""
        self.provider = VixedRequestsProvider()
        QgsApplication.processingRegistry().addProvider(self.provider)

    def initGui(self):
        self.initProcessing()

        icon = os.path.join(os.path.join(cmd_folder, 'satellite-32.ico'))
        self.action = QAction(
            QIcon(icon),
            u"Generate SAR request form", self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addPluginToMenu(u"&Vixed", self.action)
        self.iface.addToolBarIcon(self.action)

    def unload(self):
        QgsApplication.processingRegistry().removeProvider(self.provider)
        self.iface.removePluginMenu(u"&Vixed", self.action)
        self.iface.removeToolBarIcon(self.action)

    def run(self):
        processing.execAlgorithmDialog("Vixed:Generate SAR request form")