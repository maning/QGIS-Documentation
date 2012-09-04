# -*- coding: utf-8 -*-
#
# QGIS Workshop documentation build configuration file, created by
# sphinx-quickstart on Fri Jul  1 14:40:42 2011.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.append(os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = []

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']


# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'QGIS User Guide'
copyright = u'2012, QGIS project'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.7.4'
# The full version, including alpha/beta/rc tags.
release = '1.7.4'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = en

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = ['buildout', '_build']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

rst_epilog = """
.. |nix| image:: /img/en/nix.png
   :width: 1em
.. |win| image:: /img/en/win.png
   :width: 1em
.. |osx| image:: /img/en/osx.png
   :width: 1em
.. |QG| replace:: QGIS
.. |degrees| unicode:: 0x00B0
   :ltrim:
.. |geographic| image:: /img/en/geographic.png
.. |wedge| unicode:: 0x005e
.. |checkbox| image:: /img/en/checkbox.png
.. |radiobuttonon| image:: /img/en/radiobuttonon.png
.. |radiobuttonoff| image:: /img/en/radiobuttonoff.png
.. |selectnumber| image:: /img/en/selectnumber.png
.. |selectstring| image:: /img/en/selectstring.png
.. |selectstring2| image:: /img/en/selectstring2.png
.. |browsebutton| image:: /img/en/browsebutton.png
.. |selectcolor| image:: /img/en/selectcolor.png
.. |slider| image:: /img/en/slider.png
.. |inputtext| image:: /img/en/inputtext.png
.. |tab| image:: /img/en/tab.png
.. |icon_sqlanywhere| image:: img/en/plugins_sql_anywhere/sqlanywhere.png
   :width: 1.5em
.. |oracle_raster| image:: img/en/plugins_oracle_raster/oracle_raster.png
   :width: 1.5em
.. |raster_terrain| image:: img/en/plugins_raster_terrain/raster_terrain.png
   :width: 1.5em
.. |osm_load| image:: img/en/plugins_openstreetmap/osm_load.png
   :width: 1.5em
.. |osm_featureManager| image:: img/en/plugins_openstreetmap/osm_featureManager.png
   :width: 1.5em
.. |osm_download| image::  img/en/plugins_openstreetmap/osm_download.png
   :width: 1.5em
.. |osm_upload| image:: img/en/plugins_openstreetmap/osm_upload.png
   :width: 1.5em
.. |osm_import| image:: img/en/plugins_openstreetmap/osm_import.png
   :width: 1.5em
.. |osm_save| image:: img/en/plugins_openstreetmap/osm_save.png
   :width: 1.5em
.. |osm_identify| image:: img/en/plugins_openstreetmap/osm_identify.png
   :width: 1.5em
.. |osm_createPoint| image:: img/en/plugins_openstreetmap/osm_createPoint.png
   :width: 1.5em
.. |osm_createLine| image:: img/en/plugins_openstreetmap/osm_createLine.png
   :width: 1.5em
.. |osm_createPolygon| image:: img/en/plugins_openstreetmap/osm_createPolygon.png
   :width: 1.5em
.. |osm_move| image:: img/en/plugins_openstreetmap/osm_move.png
   :width: 1.5em
.. |osm_removeFeat| image:: img/en/plugins_openstreetmap/osm_removeFeat.png
   :width: 1.5em
.. |osm_createRelation| image:: img/en/plugins_openstreetmap/osm_createRelation.png
   :width: 1.5em
.. |osm_addRelation| image:: img/en/plugins_openstreetmap/osm_addRelation.png
   :width: 1.5em
.. |osm_generateTags| image:: img/en/plugins_openstreetmap/osm_generateTags.png
   :width: 1.5em
.. |osm_identify| image:: img/en/plugins_openstreetmap/osm_identify.png
   :width: 1.5em
.. |osm_editRelation| image:: img/en/plugins_openstreetmap/osm_editRelation.png
   :width: 1.5em
.. |osm_questionMark| image:: img/en/plugins_openstreetmap/osm_questionMark.png
   :width: 1.5em
.. |osm_upload| image:: img/en/plugins_openstreetmap/osm_upload.png
   :width: 1.5em 
.. |osm_save| image:: img/en/plugins_openstreetmap/osm_save.png
   :width: 1.5em
.. |osm_import| image:: img/en/plugins_openstreetmap/osm_import.png
   :width: 1.5em
.. |offline_editing_copy| image:: img/en/plugins_offline_editing/offline_editing_copy.png
   :width: 1.5em
.. |interpolation| image:: img/en/plugins_interpolation/interpolation.png
   :width: 1.5em
.. |mActionAddRasterLayer| image:: /img/en/mActionAddRasterLayer.png
   :width: 1.5em
.. |mActionAddOgrLayer| image:: /img/en/mActionAddOgrLayer.png
   :width: 1.5em
.. |mActionShowPluginManager| image:: /img/en/mActionShowPluginManager.png
.. |mActionFileNew| image:: /img/en/mActionFileNew.png
.. |mActionFileOpen| image:: /img/en/mActionFileOpen.png
.. |mActionFileSave| image:: /img/en/mActionFileSave.png
   :width: 1.5em
.. |mActionFileSaveAs| image:: /img/en/mActionFileSaveAs.png
.. |mActionSaveMapAsImage| image:: /img/en/mActionSaveMapAsImage.png
.. |mActionNewComposer| image:: /img/en/mActionNewComposer.png
.. |mActionComposerManager| image:: /img/en/mActionComposerManager.png
.. |mActionExportMapServer| image:: /img/en/mActionExportMapServer.png
   :width: 1.5em
.. |mActionSaveAsSVG| image:: /img/en/mActionSaveAsSVG.png
   :width: 1.5em
.. |mActionSaveAsPDF| image:: /img/en/mActionSaveAsPDF.png
   :width: 1.5em
.. |mActionFilePrint| image:: /img/en/mActionFilePrint.png
   :width: 1.5em
.. |mActionAddArrow| image:: /img/en/mActionAddArrow.png
   :width: 1.5em
.. |mActionAddBasicShape| image:: /img/en/mActionAddBasicShape.png
   :width: 1.5em
.. |mActionAddLegend| image:: /img/en/mActionAddLegend.png
   :width: 1.5em
.. |mActionAddMap| image:: /img/en/mActionAddMap.png
   :width: 1.5em
.. |mActionLabel| image:: /img/en/mActionLabel.png
   :width: 1.5em
.. |mActionScaleBar| image:: /img/en/mActionScaleBar.png
   :width: 1.5em
.. |mActionSelectPan| image:: /img/en/mActionSelectPan.png
   :width: 1.5em
.. |mActionGroupItems| image:: /img/en/mActionGroupItems.png
   :width: 1.5em
.. |mActionUnGroupItems| image:: /img/en/mActionUnGroupItems.png
   :width: 1.5em
.. |mActionRaiseItems| image:: /img/en/mActionRaiseItems.png
   :width: 1.5em
.. |mActionLowerItems| image:: /img/en/mActionLowerItems.png
   :width: 1.5em
.. |mActionMoveItemContent| image:: /img/en/mActionMoveItemContent.png
   :width: 1.5em
.. |mActionMoveItemsToTop| image:: /img/en/mActionMoveItemsToTop.png
   :width: 1.5em
.. |mActionMoveItemsToBottom| image:: /img/en/mActionMoveItemsToBottom.png
   :width: 1.5em
.. |mActionAlignLeft|  image:: /img/en/mActionAlignLeft.png
   :width: 1.5em
.. |mActionAlignRight|  image:: /img/en/mActionAlignRight.png
   :width: 1.5em
.. |mActionAlignHCenter|  image:: /img/en/mActionAlignHcenter.png
   :width: 1.5em
.. |mActionAlignVCenter|  image:: /img/en/mActionAlignVCenter.png
   :width: 1.5em
.. |mActionAlignTop|  image:: /img/en/mActionAlignTop.png
   :width: 1.5em
.. |mActionAlignBottom|  image:: /img/en/mActionAlignBottom.png
   :width: 1.5em
.. |mIconLock|  image:: /img/en/mIconLock.png
   :width: 1.5em
.. |mActionFileExit| image:: /img/en/mActionFileExit.png
.. |mActionUndo| image:: /img/en/mActionUndo.png
   :width: 1.5em
.. |mActionRedo| image:: /img/en/mActionRedo.png
   :width: 1.5em
.. |mActionSelect| image:: /img/en/mActionSelect.png
   :width: 1.5em
.. |mActionEditCut| image:: /img/en/mActionEditCut.png
   :width: 1.5em
.. |mActionEditCopy| image:: /img/en/mActionEditCopy.png
   :width: 1.5em
.. |mActionEditPaste| image:: /img/en/mActionEditPaste.png
   :width: 1.5em
.. |mActionDeleteAttribute| image:: img/en/mActionDeleteAttribute.png
   :width: 1.5em
.. |mActionDeleteSelected| image:: /img/en/mActionDeleteSelected.png
   :width: 1.5em
.. |mActionDeleteVertex| image:: /img/en/mActionDeleteVertex.png
   :width: 1.5em
.. |mActionSimplify| image:: /img/en/mActionSimplify.png
   :width: 2em
.. |mActionAddRing| image:: /img/en/mActionAddRing.png
   :width: 2em
.. |mActionAddIsland| image:: /img/en/mActionAddIsland.png
   :width: 2em
.. |mActionDeleteRing| image:: /img/en/mActionDeleteRing.png
   :width: 2em
.. |mActionDeletePart| image:: /img/en/mActionDeletePart.png
   :width: 2em
.. |mActionReshape| image:: /img/en/mActionReshape.png
   :width: 1.5em
.. |mActionSplitFeatures| image:: /img/en/mActionSplitFeatures.png
   :width: 1.5em
.. |mActionMergeFeatures| image:: /img/en/mActionMergeFeatures.png
   :width: 1.5em
.. |mergeFeats| image:: /img/en/mActionMergeFeatures.png
   :width: 1.5em
.. |mActionNodeTool| image:: /img/en/mActionNodeTool.png
   :width: 1.5em
.. |mActionSelectedToTop| image:: /img/en/mActionSelectedToTop.png
   :width: 1.5em
.. |mActionInvertSelection| image:: /img/en/mActionInvertSelection.png
   :width: 1.5em
.. |mActionCopySelected| image:: /img/en/mActionCopySelected.png
   :width: 1.5em
.. |mActionZoomToSelected| image:: /img/en/mActionZoomToSelected.png
   :width: 1em
.. |mActionNewAttribute| image:: /img/en/mActionNewAttribute.png
   :width: 1.5em
.. |mActionCalculateField| image:: /img/en/mActionCalculateField.png
   :width: 1.5em
.. |mActionRotatePointSymbols| image:: /img/en/mActionRotatePointSymbols.png
   :width: 1.5em
.. |mActionToggleEditing| image:: /img/en/mActionToggleEditing.png
   :width: 1.5em
.. |mActionCapturePoint| image:: /img/en/mActionCapturePoint.png
   :width: 1.5em
.. |mActionCaptureLine| image:: /img/en/mActionCaptureLine.png
   :width: 1.5em
.. |mActionCapturePolygon| image:: /img/en/mActionCapturePolygon.png
   :width: 1.5em
.. |mActionMoveFeature| image:: /img/en/mActionMoveFeature.png
   :width: 1.5em
.. |mActionPan| image:: /img/en/mActionPan.png
   :width: 1.5em
.. |mActionZoomIn| image:: /img/en/mActionZoomIn.png
   :width: 1.5em
.. |mActionZoomOut| image:: /img/en/mActionZoomOut.png
   :width: 1.5em
.. |mActionIdentify| image:: /img/en/mActionIdentify.png
   :width: 1.5em
.. |mActionNewVectorLayer| image:: /img/en/mActionNewVectorLayer.png
   :width: 1.5em
.. |mActionZoomFullExtent| image:: /img/en/mActionZoomFullExtent.png
   :width: 1.5em
.. |mActionZoomToLayer| image:: /img/en/mActionZoomToLayer.png
   :width: 1.5em
.. |mActionZoomToSelected| image:: /img/en/mActionZoomToSelected.png
   :width: 1.5em
.. |mActionZoomLast| image:: /img/en/mActionZoomLast.png
   :width: 1.5em
.. |mActionZoomNext| image:: /img/en/mActionZoomNext.png
   :width: 1.5em
.. |mActionMapTips| image:: /img/en/mActionMapTips.png
   :width: 1.5em
.. |mActionNewBookmark| image:: /img/en/mActionNewBookmark.png
   :width: 1.5em
.. |mActionShowBookmarks| image:: /img/en/mActionShowBookmarks.png
   :width: 1.5em
.. |mActionDraw| image:: /img/en/mActionDraw.png
   :width: 1.5em
.. |mActionAddNonDbLayer| image:: /img/en/mActionAddNonDbLayer.png
   :width: 1.5em
.. |mActionAddLayer| image:: /img/en/mActionAddLayer.png
   :width: 1.5em
.. |mActionAddSpatiaLiteLayer| image:: /img/en/mActionAddSpatiaLiteLayer.png
   :width: 1.5em
.. |mActionAddWmsLayer| image:: /img/en/mActionAddWmsLayer.png
   :width: 1.5em
.. |mActionOpenTable| image:: /img/en/mActionOpenTable.png
   :width: 1.5em
.. |mActionRemoveLayer| image:: /img/en/mActionRemoveLayer.png
   :width: 1.5em
.. |mActionLabeling| image:: /img/en/mActionLabeling.png
   :width: 1.5em
.. |mActionInOverview| image:: /img/en/mActionInOverview.png
   :width: 1.5em
.. |mActionAddAllToOverview| image:: /img/en/mActionAddAllToOverview.png
   :width: 1.5em
.. |mActionRemoveAllFromOverview| image:: /img/en/mActionRemoveAllFromOverview.png
   :width: 1.5em
.. |RemoveAllOVerview| image:: /img/en/mActionRemoveAllFromOverview.png
   :width: 1.5em
.. |mActionShowAllLayers| image:: /img/en/mActionShowAllLayers.png
   :width: 1.5em
.. |mActionHideAllLayers| image:: /img/en/mActionHideAllLayers.png
   :width: 1.5em
.. |mActionProjectProperties| image:: /img/en/mActionProjectProperties.png
   :width: 1.5em
.. |mActionCustomProjection| image:: /img/en/mActionCustomProjection.png
   :width: 1.5em
.. |mActionOptions| image:: /img/en/mActionOptions.png
   :width: 1em
.. |mActionHelpContents| image:: /img/en/mActionHelpContents.png
   :width: 1.5em
.. |mActionQgisHomePage| image:: /img/en/mActionQgisHomePage.png
   :width: 1.5em
.. |mActionCheckQgisVersion| image:: /img/en/mActionCheckQgisVersion.png
   :width: 1.5em
.. |mActionHelpAbout| image:: /img/en/mActionHelpAbout.png
   :width: 1.5em
.. |mActionHelpSponsors| image:: /img/en/mActionHelpSponsors.png
   :width: 1.5em
.. |mActionTextAnnotation| image:: /img/en/mActionTextAnnotation.png
   :width: 1.5em
.. |mActionAnnotation| image:: /img/en/mActionAnnotation.png
   :width: 1.5em
.. |mIconStopRendering| image:: /img/en/mIconStopRendering.png
   :width: 1.5em
.. |mIconProjectionDisabled| image:: /img/en/mIconProjectionDisabled.png
   :width: 1.5em
.. |mIconProjectionEnabled| image:: /img/en/mIconProjectionEnabled.png
   :width: 1.5em
.. |mActionMeasure| image:: /img/en/mActionMeasure.png
   :width: 1.5em
.. |mActionMeasureArea| image:: /img/en/mActionMeasureArea.png
   :width: 1.5em
.. |mActionMeasureAngle| image:: /img/en/mActionMeasureAngle.png
   :width: 1.5em
.. |spiticon| image:: /plugins/img/en/plugins_spit/spiticon.png
.. |mActionOptions| image:: /img/en/mActionOptions.png
   :width: 1.5em
.. |mActionSelectRectangle| image:: /img/en/mActionSelectRectangle.png
   :width: 1.5em
.. |mActionSelectPolygon| image:: /img/en/mActionSelectPolygon.png
   :width: 1.5em
.. |mActionSelectFreehand| image:: /img/en/mActionSelectFreehand.png
   :width: 1.5em
.. |mActionSelectRadius| image:: /img/en/mActionSelectRadius.png
   :width: 1.5em
.. |mActionDeselectAll| image:: /img/en/mActionDeselectAll.png
   :width: 1.5em
.. |mActionFormAnnotation| image:: /img/en/mActionFormAnnotation.png
   :width: 1.5em
.. |mActionContextHelp| image:: /img/en/mActionContextHelp.png
   :width: 1.5em
.. |mActionFolder| image:: /img/en/mActionFolder.png
   :width: 1.5em
.. |mIconNew| image:: /img/en/mIconNew.png
   :width: 1.5em
.. |gpstrack_barchart| image:: /introduction/img/en/gpstrack_barchart.png
   :width: 1.5em
.. |gpstrack_polarchart| image:: /introduction/img/en/gpstrack_polarchart.png
   :width: 1.5em
.. |gps_importer| image:: img/en/plugins_gps/gps_importer.png
   :width: 1.5em
.. |wfs| image:: /img/en/wfs.png
   :width: 1.5em
.. |matrix| image:: img/en/plugins_ftools/matrix.png
   :width: 3em
.. |sum_lines| image:: img/en/plugins_ftools/sum_lines.png
   :width: 3em
.. |sum_points| image:: img/en/plugins_ftools/sum_points.png
   :width: 3em
.. |unique| image:: img/en/plugins_ftools/unique.png
   :width: 3em
.. |basic_statistics| image:: img/en/plugins_ftools/basic_statistics.png
   :width: 3em
.. |neighbor| image:: img/en/plugins_ftools/neighbour.png
   :width: 3em
.. |mean| image:: img/en/plugins_ftools/mean.png
   :width: 3em
.. |intersections| image:: img/en/plugins_ftools/intersections.png
   :width: 3em
.. |random_selection| image:: img/en/plugins_ftools/random_selection.png
   :width: 3em
.. |sub_selection| image:: img/en/plugins_ftools/sub_selection.png
   :width: 3em
.. |random_points| image:: img/en/plugins_ftools/random_points.png
   :width: 3em
.. |regular_points| image:: img/en/plugins_ftools/regular_points.png
   :width: 3em
.. |vector_grid| image:: img/en/plugins_ftools/vector_grid.png
   :width: 3em
.. |select_location| image:: img/en/plugins_ftools/select_location.png
   :width: 3em
.. |layer_extent| image:: img/en/plugins_ftools/layer_extent.png
   :width: 3em
.. |convex_hull| image:: img/en/plugins_ftools/convex_hull.png
   :width: 3em
.. |buffer| image:: img/en/plugins_ftools/buffer.png
   :width: 3em
.. |intersect| image:: img/en/plugins_ftools/intersect.png
   :width: 3em
.. |union| image:: img/en/plugins_ftools/union.png
   :width: 3em
.. |sym_difference| image:: img/en/plugins_ftools/sym_difference.png
   :width: 3em
.. |clip| image:: img/en/plugins_ftools/clip.png
   :width: 3em
.. |difference| image:: img/en/plugins_ftools/difference.png
   :width: 3em
.. |dissolve| image:: img/en/plugins_ftools/dissolve.png
   :width: 3em
.. |check_geometry| image::  img/en/plugins_ftools/check_geometry.png
   :width: 3em
.. |export_geometry| image:: img/en/plugins_ftools/export_geometry.png
   :width: 3em
.. |centroids| image:: img/en/plugins_ftools/centroids.png
   :width: 3em
.. |delaunay| image:: img/en/plugins_ftools/delaunay.png
   :width: 3em
.. |simplify| image:: img/en/plugins_ftools/simplify.png
   :width: 3em
.. |multi_to_single| image:: img/en/plugins_ftools/multi_to_single.png
   :width: 3em
.. |single_to_multi| image:: img/en/plugins_ftools/single_to_multi.png
   :width: 3em
.. |to_lines| image:: img/en/plugins_ftools/to_lines.png
   :width: 3em
.. |lines_to|  image:: img/en/plugins_ftools/lines_to.png
   :width: 3em
.. |extract_nodes| image:: img/en/plugins_ftools/extract_nodes.png
   :width: 3em
.. |export_projection| image:: img/en/plugins_ftools/export_projection.png
   :width: 3em
.. |define_projection| image:: img/en/plugins_ftools/define_projection.png
   :width: 3em
.. |join_location| image:: img/en/plugins_ftools/join_location.png
   :width: 3em
.. |split_layer| image:: img/en/plugins_ftools/split_layer.png
   :width: 3em
.. |merge_shapes| image:: img/en/plugins_ftools/merge_shapes.png
   :width: 3em
.. |event_browser| image:: img/en/plugins_evis/event_browser.png
   :width: 1.5em
.. |event_id| image:: img/en/plugins_evis/event_id.png
   :width: 1.5em
.. |evis_connect| image:: img/en/plugins_evis/evis_connect.png
   :width: 1.5em
.. |evis_file| image:: img/en/plugins_evis/evis_file.png
   :width: 1.5em
.. |dxf2shp_converter| image:: img/en/plugins_dxf2shape_converter/dxf2shp_converter.png
   :width: 1.5em
.. |measure_line| image:: /introduction/img/en/measure_line.png
   :width: 22em
.. |measure_area| image:: /introduction/img/en/measure_area.png
   :width: 22em
.. |measure_angle| image:: /introduction/img/en/measure_angle.png
   :width: 18em
.. |gpstrack_main| image:: /introduction/img/en/gpstrack_main.png
   :width: 15em
.. |gpstrack_stren| image:: /introduction/img/en/gpstrack_stren.png
   :width: 15em
.. |gpstrack_polar| image:: /introduction/img/en/gpstrack_polar.png
   :width: 15em
.. |grass_open_mapset| image:: /grass_integration/img/en/grass_open_mapset.png
   :width: 1.5em
.. |grass_new_mapset| image:: /grass_integration/img/en/grass_new_mapset.png
   :width: 1.5em
.. |grass_close_mapset| image:: /grass_integration/img/en/grass_close_mapset.png
   :width: 1.5em
.. |grass_add_vector| image:: /grass_integration/img/en/grass_add_vector.png
   :width: 1.5em
.. |grass_add_raster| image:: /grass_integration/img/en/grass_add_raster.png
   :width: 1.5em
.. |grass_new_vector_layer| image:: /grass_integration/img/en/grass_new_vector_layer.png
   :width: 1.5em
.. |grass_edit| image:: /grass_integration/img/en/grass_edit.png
   :width: 1.5em
.. |grass_tools| image:: /grass_integration/img/en/grass_tools.png
   :width: 1.5em
.. |grass_region| image:: /grass_integration/img/en/grass_region.png
   :width: 1.5em
.. |grass_region_edit| image:: /grass_integration/img/en/grass_region_edit.png
   :width: 1.5em
.. |grass_open_mapset| image:: /grass_integration/img/en/grass_open_mapset.png
   :width: 1.5em
.. |grass_new_point| image:: /grass_integration/img/en/grass_new_point.png
   :width: 1.5em
.. |grass_new_line| image:: /grass_integration/img/en/grass_new_line.png
   :width: 1.5em
.. |grass_new_boundary| image:: /grass_integration/img/en/grass_new_boundary.png
   :width: 1.5em
.. |grass_new_centroid| image:: /grass_integration/img/en/grass_new_centroid.png
   :width: 1.5em
.. |grass_move_vertex| image:: /grass_integration/img/en/grass_move_vertex.png
   :width: 1.5em
.. |grass_add_vertex| image:: /grass_integration/img/en/grass_add_vertex.png
   :width: 1.5em
.. |grass_delete_vertex| image:: /grass_integration/img/en/grass_delete_vertex.png
   :width: 1.5em
.. |grass_move_line| image:: /grass_integration/img/en/grass_move_line.png
   :width: 1.5em
.. |grass_split_line| image:: /grass_integration/img/en/grass_split_line.png
   :width: 1.5em
.. |grass_delete_line| image:: /grass_integration/img/en/grass_delete_line.png
   :width: 1.5em
.. |grass_edit_attributes| image:: /grass_integration/img/en/grass_edit_attributes.png
   :width: 1.5em
.. |grass_close_edit| image:: /grass_integration/img/en/grass_close_edit.png
   :width: 1.5em
.. |grass_add_map| image:: /grass_integration/img/en/grass_add_map.png
   :width: 1.5em
.. |grass_copy_map| image:: /grass_integration/img/en/grass_copy_map.png
   :width: 1.5em
.. |grass_rename_map| image:: /grass_integration/img/en/grass_rename_map.png
   :width: 1.5em
.. |grass_delete_map| image:: /grass_integration/img/en/grass_delete_map.png
   :width: 1.5em
.. |grass_set_region| image:: /grass_integration/img/en/grass_set_region.png
   :width: 1.5em
.. |grass_refresh| image:: /grass_integration/img/en/grass_refresh.png
   :width: 1.5em
"""


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
#html_theme = 'sphinxdoc'
html_theme = 'sphinxdoc'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['../themes']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['img']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_use_modindex = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'QGISUserGuide'


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('user_guide', 'QGISUserGuide.tex', u'QGIS Workshop Documentation',
   u'Greg Corradini and Aaron Racicot', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True

# -- Options for PDF output ----------------------------------------------------
 
# Grouping the document tree into PDF files. List of tuples
# (source start file, target name, title, author).
pdf_documents = [
    ('user_guide', u'QGISUserGuide', u'QGIS User Guide', u'QGIS Project'),
]

# A comma-separated list of custom stylesheets. Example:
pdf_stylesheets = ['sphinx','kerning','a4']

# Create a compressed PDF
# Use True/False or 1/0
# Example: compressed=True
#pdf_compressed=False

# A colon-separated list of folders to search for fonts. Example:
# pdf_font_path=['/usr/share/fonts', '/usr/share/texmf-dist/fonts/']
# Language to be used for hyphenation support
#pdf_language="en_EN"

# If false, no index is generated.
#pdf_use_index = True

# If false, no modindex is generated.
#pdf_use_modindex = True

# If false, no coverpage is generated.
#pdf_use_coverpage = True

locale_dirs = ['translated']


