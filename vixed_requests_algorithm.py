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

from qgis.PyQt.QtCore import QCoreApplication
from processing.algs.qgis.QgisAlgorithm import QgisAlgorithm
from qgis.core import (QgsProcessing,
                       QgsFeatureSink,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterFeatureSink,
                       QgsProcessingParameterExtent,
                       QgsProcessingParameterString,
                       QgsProcessingParameterFileDestination,
                       QgsProcessingParameterEnum,
                       QgsProcessingParameterNumber)


# class VixedRequestsAlgorithm(QgsProcessingAlgorithm):
class VixedRequestsAlgorithm(QgisAlgorithm):
    """
    This is an example algorithm that takes a vector layer and
    creates a new identical one.

    It is meant to be used as an example of how to create your own
    algorithms and explain methods and variables used to do it. An
    algorithm like this will be available in all elements, and there
    is not need for additional work.

    All Processing algorithms should extend the QgsProcessingAlgorithm
    class.
    """

    # Constants used to refer to parameters and outputs. They will be
    # used when calling the algorithm from another algorithm, or when
    # calling from the QGIS console.

    OUTPUT = 'OUTPUT'
    INPUT = 'INPUT'
    EXTENT = 'PROJWIN'
    OPTIONS = 'OPTIONS'
    PROCESSORS = "PROCESSORS"
    ESTIMATED_FILESIZE = "Estimated filesize"
    RESOLUTION = "RESOLUTION"
    TIMEDELTA = 'TIMEDELTA'
    #
    # def group(self):
    #     return self.tr('Vixed')
    #
    # def groupId(self):
    #     return 'Vixed'


    def initAlgorithm(self, config):
        """
        Here we define the inputs and output of the algorithm, along
        with some other properties.
        """

        processors = [self.tr('SAR')]

        self.addParameter(QgsProcessingParameterEnum(
            self.PROCESSORS,
            self.tr('Vixed Processors'),
            options=processors, defaultValue="SAR"))

        # We add the input vector features source. It can have any kind of
        # geometry.
        # self.addParameter(
        #     QgsProcessingParameterFeatureSource(
        #         self.INPUT,
        #         self.tr('Input layer'),
        #         [QgsProcessing.TypeVectorAnyGeometry]
        #     )
        # )

        self.addParameter(
            QgsProcessingParameterExtent(
                self.EXTENT,
                self.tr('Select extent')
            )
        )

        self.addParameter(QgsProcessingParameterNumber(
            self.RESOLUTION,
            self.tr(
                'Spatial resolution (meters per pixel)'),
            defaultValue=500,
            minValue=50,
            type=QgsProcessingParameterNumber.Integer
        ))

        self.addParameter(QgsProcessingParameterNumber(
            self.TIMEDELTA,
            self.tr(
                'Temporal aggregation window (hours)'),
            defaultValue=24,
            minValue=1,
            type=QgsProcessingParameterNumber.Integer
        ))

        self.addParameter(
            QgsProcessingParameterFileDestination(self.OUTPUT, self.tr('Sar request for Vixed'), self.tr('JSON files (*.json)')))

    def processAlgorithm(self, parameters, context, feedback):
        """
        Here is where the processing itself takes place.
        """

        # Retrieve the feature source and sink. The 'dest_id' variable is used
        # to uniquely identify the feature sink, and must be included in the
        # dictionary returned by the processAlgorithm function.
        # source = self.parameterAsSource(parameters, self.INPUT, context)
        # (sink, dest_id) = self.parameterAsSink(parameters, self.OUTPUT,
        #         context, source.fields(), source.wkbType(), source.sourceCrs())
        #
        # # Compute the number of steps to display within the progress bar and
        # # get features from source
        # total = 100.0 / source.featureCount() if source.featureCount() else 0
        # features = source.getFeatures()
        #
        # for current, feature in enumerate(features):
        #     # Stop the algorithm if cancel button has been clicked
        #     if feedback.isCanceled():
        #         break
        #
        #     # Add a feature in the sink
        #     sink.addFeature(feature, QgsFeatureSink.FastInsert)
        #
        #     # Update the progress bar
        #     feedback.setProgress(int(current * total))

        # Return the results of the algorithm. In this case our only result is
        # the feature sink which contains the processed features, but some
        # algorithms may return multiple feature sinks, calculated numeric
        # statistics, etc. These should all be included in the returned
        # dictionary, with keys matching the feature corresponding parameter
        # or output names.
        # return {self.OUTPUT: dest_id}

        contents = self.EXTENT

        # contents = load_request_file
        # update extent

        extent = self.parameterAsFileOutput(parameters, self.EXTENT, context)

        print("CONTENTS: ", contents)

        output = self.parameterAsFileOutput(parameters, self.OUTPUT, context)

        with open(output, mode="w") as output_json:
            output_json.write(extent)

        filesize = "20MB"

        return {self.OUTPUT: output, self.ESTIMATED_FILESIZE: filesize}

    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'Generate Vixed SAR request form'

    def displayName(self):
        """
        Returns the translated algorithm name, which should be used for any
        user-visible display of the algorithm name.
        """
        return self.tr(self.name())

    def group(self):
        """
        Returns the name of the group this algorithm belongs to. This string
        should be localised.
        """
        return self.tr(self.groupId())

    def groupId(self):
        """
        Returns the unique ID of the group this algorithm belongs to. This
        string should be fixed for the algorithm, and must not be localised.
        The group id should be unique within each provider. Group id should
        contain lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'Vixed'

    def tr(self, string):
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return VixedRequestsAlgorithm()