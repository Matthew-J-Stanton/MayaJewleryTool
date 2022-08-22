import logging
import os
#logging.basicConfig()
log = logging.getLogger("Jewlery Tool")
fileName = os.path.splitext(os.path.basename(__file__))[0]

log.debug('nameJewleryPopup loading')
try:
    log.debug('trying to import PySide 2 into {}'.format(fileName))
    from PySide2.QtCore import *
    from PySide2.QtGui import *
    from PySide2.QtWidgets import *
    # So we import wrapInstance from sip and alias it to wrapInstance so that it's the same as the others
    from shiboken2 import wrapInstance
    log.debug('Using PySide2 and Shiboken2 in {}'.format(fileName))


except:
    log.debug('PySide 2 not avalable')
    try:
        log.debug('trying to import PySide into {}'.format(fileName))
        from PySide.QtCore import *
        from PySide.QtGui import *
        from PySide.QtWidgets import *
        # So we import wrapInstance from sip and alias it to wrapInstance so that it's the same as the others
        from shiboken import wrapinstance 
        log.debug('Using PySide and Shiboken in {}'.format(fileName))


    except:
        log.debug('Pyside not avalable')
        try:
            log.debug('trying to import PyQt5 into {}'.format(fileName))
            from PyQt5.QtCore import *
            from PyQt5.QtGui import *
            from PyQt5.QtWidgets import *
            # So we import wrapInstance from sip and alias it to wrapInstance so that it's the same as the others
            from sip import wrapinstance as wrapInstance
            log.debug('Using PyQt5 and sip in {}'.format(fileName))

        except:
            log.debug('PyQt5 not avalable')
            log.debug('trying to import PyQt4 into {}'.format(fileName))
            from PyQt4.QtCore import *
            from PyQt4.QtGui import *
            from PyQt4.QtWidgets import *
            # So we import wrapInstance from sip and alias it to wrapInstance so that it's the same as the others
            from sip import wrapinstance as wrapInstance
            log.debug('Using PyQt4 and sip in {}'.format(fileName))

import pymel.core as pm
log.debug('Imported pymel.core')
import maya.cmds as cmds
log.debug('imported maya.cmds')

import maya.api.OpenMaya as om

log.info("Imported libraries into {}".format(fileName))
log.info('Creating Jhumka')

plugin_root = os.environ.get("JEWLERYTOOLPLUGIN_ROOT")
houdiniFilesPath = plugin_root + "/houdini-files/"


class jhumka():
    def __init__(self, controls, name):
        log.info('initializing jhumka called {}'.format(name))
        self.controls = controls
        self.name = name

        log.debug('getting node to link to jhumka')
        self.nodeName = "{}_JhumkaAttributesNode".format(name)
        log.info('node name is {} for Jhumka {}'.format(self.nodeName, name))
        self.loadAsset()

    def loadAsset(self):
        log.info('loading houdini asset using load Asset function')
        self.attributeList = []
        self.attributeListCB = []
        self.attributeListDT = []
        log.debug('attribute lists setup up for {}'.format(self.name))
        log.debug('loading jhumka Houdini asset')
        self.asset = cmds.houdiniAsset(loadAsset=[houdiniFilesPath+"Jhumka_tool.hdanc", "Sop/Jhumka_tool"])
        dagPath = om.MDagPath()
        #pm.setAttr("Jhumka_tool1_0Shape.displayColors", 0)
        log.info('asset loaded as {}'.format(self.asset))
        pm.select(self.asset)
        
        jhumkaName = self.name+"_Jhumka"
        log.debug('renaming jhumka asset to {}'.format(jhumkaName))
        pm.rename( self.asset,  jhumkaName)

        self.jhumkaName = pm.ls( selection=True, shortNames=True )[0]
        log.info('jhumka name set as {}'.format(self.jhumkaName))
        strJhumkaName = str(self.jhumkaName)
        log.debug('getting Jhumka children')
        tool = cmds.listRelatives(strJhumkaName)
        children = cmds.listRelatives(tool)
        log.debug('{} child found : {}'.format(strJhumkaName, tool))
        log.debug('{} children found : {}'.format(tool, children))

        toolName = strJhumkaName+"_tool"
        pm.rename( tool, toolName )

        log.debug('Jhumka child {} renamed to {}'.format(tool, toolName))

        counter = 0

        log.debug('renaming tool children')
        for each in children:
            childName = toolName + "1_{}".format(counter)
            
            pm.rename( each, childName )
            log.debug('tool child {} renamed to {}'.format(each, childName))

            pm.setAttr("{}Shape.displayColors".format(childName), 0)
            log.debug('setting display colour {}Shape.displayColors set to 0'.format(childName))

            counter += 1
        
        
        
        #print("ASSET - {}".format(asset))

        #print("Type - {}".format(type(self.asset)))
        #cmds.sets(self.asset, forceElement="initialShadingGroup")
        #pm.hyperShade(assign = 'mySurfaceShader')
        #cmds.setAttr("{}_0Shape.displayColors".format(self.asset), 0)

        rows = "{}.houdiniAssetParm_jhumka_Rows".format(self.jhumkaName)
        log.debug('got the rows parameter of the Houdini asset: {} '.format(rows))
        nodeOutRows = "{}.outRows".format(self.nodeName)
        log.debug('got the outRows parameter of the attributeNode: {} '.format(nodeOutRows))
        localList = [rows, nodeOutRows]
        self.attributeList.append(localList)
        log.debug('added Houdini and node attribute rows parameter to attributeListMainTab')
        log.debug('houdini asset rows is - {} | node outRows is {}'.format(rows, nodeOutRows))

        columns = "{}.houdiniAssetParm_jhumka_Columns".format(self.jhumkaName)
        log.debug('got the columns parameter of the Houdini asset: {} '.format(columns))
        nodeOutColumns = "{}.outColumns".format(self.nodeName)
        log.debug('got the outColumns parameter of the attributeNode: {} '.format(nodeOutColumns))
        #cmds.connectAttr( "tes_JhumkaAttributesNode.columns", "tes_Jhumka.houdiniAssetParm_jhumka_Columns", f=0 )
        #cmds.connectAttr( nodeOutColumns, columns, f=1)
        localList = [columns, nodeOutColumns]
        self.attributeList.append(localList)
        log.debug('added Houdini and node attribute columns parameter to attributeListMainTab')
        log.debug('houdini asset columns is - {} | node outColumns is {} | for jewlery {}'.format(columns, nodeOutColumns, self.name))

        scale = "{}.houdiniAssetParm_scale".format(self.jhumkaName)
        log.debug('got the scale parameter of the Houdini asset: {} '.format(scale))
        nodeOutScale = "{}.outScale".format(self.nodeName)
        log.debug('got the outScale parameter of the attributeNode: {} '.format(nodeOutScale))
        localList = [scale, nodeOutScale]
        self.attributeList.append(localList)
        log.debug('added Houdini and node attribute scale parameter to attributeListMainTab')
        log.debug('houdini asset scale is - {} | node outScale is {} | for jewlery {}'.format(scale, nodeOutScale, self.name))

        stretch = "{}.houdiniAssetParm_jhumkaStretch".format(self.jhumkaName)
        log.debug('got the stretch parameter of the Houdini asset: {} '.format(stretch))
        nodeOutStretch = "{}.outStretch".format(self.nodeName)
        log.debug('got the outStretch parameter of the attributeNode: {} '.format(nodeOutStretch))
        localList = [stretch, nodeOutStretch]
        self.attributeList.append(localList)
        log.debug('added Houdini and node attribute stretch parameter to attributeListMainTab')
        log.debug('houdini asset stretch is - {} | node outStretch is {} | for jewlery {}'.format(stretch, nodeOutStretch, self.name))

        delAmount = "{}.houdiniAssetParm_jhumkaDeleteAmount".format(self.jhumkaName)
        log.debug('got the delete amount parameter of the Houdini asset: {} '.format(delAmount))
        nodeOutDelAmount = "{}.outJhumkaAmount".format(self.nodeName)
        log.debug('got the outJhumkaAmount parameter of the attributeNode: {} '.format(nodeOutDelAmount))
        localList = [delAmount, nodeOutDelAmount]
        self.attributeList.append(localList)
        log.debug('added Houdini and node attribute jhumka amount parameter to attributeListMainTab')
        log.debug('houdini asset delAmount is - {} | node outJhumkaAmount is {} | for jewlery {}'.format(delAmount, nodeOutDelAmount, self.name))

        dangleSize = "{}.houdiniAssetParm_danglingBallsScale".format(self.jhumkaName)
        log.debug('got the dangle size parameter of the Houdini asset: {} '.format(dangleSize))
        nodeOutDangleSize = "{}.outDangleSize".format(self.nodeName)
        log.debug('got the outDangleSizes parameter of the attributeNode: {} '.format(nodeOutDangleSize))
        localList = [dangleSize, nodeOutDangleSize]
        self.attributeList.append(localList)
        log.debug('added Houdini and node attribute dangle size parameter to attributeListMainTab')
        log.debug('houdini asset dangleSize is - {} | node outDangleSize is {} | for jewlery {}'.format(dangleSize, nodeOutDangleSize, self.name))

        doubleRings = "{}.houdiniAssetParm_doubleRings".format(self.jhumkaName)
        # localList = [doubleRings, self.checkBox]
        #self.attributeList.append(localList)

        jewelSize = "{}.houdiniAssetParm_jewelSize".format(self.jhumkaName)
        log.debug('got the jewel size parameter of the Houdini asset: {} '.format(jewelSize))
        nodeOutJewelSize = "{}.outJewelSize".format(self.nodeName)
        log.debug('got the outJewelSize parameter of the attributeNode: {} '.format(nodeOutJewelSize))
        localList = [jewelSize, nodeOutJewelSize]
        self.attributeList.append(localList)
        log.debug('added Houdini and node attribute jewel size parameter to attributeListMainTab')
        log.debug('houdini asset jewelSize is - {} | node outJewelSize is {} | for jewlery {}'.format(jewelSize, nodeOutJewelSize, self.name))

        numOfSections = "{}.houdiniAssetParm_numberOfSections".format(self.jhumkaName)
        log.debug('got the number of sections parameter of the Houdini asset: {} '.format(numOfSections))
        nodeOutNumOfSections = "{}.outNumOfSec".format(self.nodeName)
        log.debug('got the outNumOfSec parameter of the attributeNode: {} '.format(nodeOutNumOfSections))
        localList = [numOfSections, nodeOutNumOfSections]
        self.attributeList.append(localList)
        log.debug('added Houdini and node attribute number of sections parameter to attributeListMainTab')
        log.debug('houdini asset number of sections is - {} | node outNumOfSections is {} | for jewlery {}'.format(numOfSections, nodeOutNumOfSections, self.name))


        hookScale = "{}.houdiniAssetParm_hookScale".format(self.jhumkaName)
        log.debug('got the hook scale parameter of the Houdini asset: {} '.format(hookScale))
        nodeOutHookScale = "{}.outHookCircleRad".format(self.nodeName)
        log.debug('got the outHookCircleRadius parameter of the attributeNode: {} '.format(nodeOutHookScale))
        localList = [hookScale, nodeOutHookScale]
        self.attributeList.append(localList)
        log.debug('added Houdini and node attribute hook sca;e parameter to attributeListMainTab')
        log.debug('houdini asset hook scale is - {} | node outHookScale is {} | for jewlery {}'.format(hookScale, nodeOutHookScale, self.name))

        blendJhumka = "{}.houdiniAssetParm_blendToggle".format(self.jhumkaName)
        log.debug('got the blend jhumka parameter of the Houdini asset: {} '.format(blendJhumka))
        nodeOutBlendJhumka = "{}.outBlendJhumka".format(self.nodeName)
        log.debug('got the outBlendJhumka parameter of the attributeNode: {} '.format(nodeOutBlendJhumka))
        log.debug('houdini asset blend jhumka check box is - {} | node outBlendJhumka is {} | for jewlery {}'.format(blendJhumka, nodeOutBlendJhumka, self.name))

        log.debug('connecting {} to {}'.format( nodeOutBlendJhumka, blendJhumka))
        cmds.connectAttr( nodeOutBlendJhumka, blendJhumka, )
        log.debug('connected {} to {}'.format( nodeOutBlendJhumka, blendJhumka))
        

        self.setupSignalSlots()

        self.setupMainTab()

        self.setupHookTab()

        self.setupTabSignalSlots(self.attributeListMainTab)
         #setAttr("Jhumka_tool1.houdiniAssetParm_jhumka_Rows" 32)
         #setAttr "Jhumka_tool1.houdiniAssetParm_jhumka_Rows" 36;
 
    

    def setupSignalSlots(self):
        log.info('setting up signals and slots for the Jhumka')

        for each in self.attributeList:
            log.debug("connecting {} to {}".format(str(each[1]), str(each[0])))
            cmds.connectAttr( each[1], each[0], f=1)
            log.info("connected {} to {}".format(str(each[1]), str(each[0])))

    def setupMainTab(self):
        log.debug('getting main tab names for Houdini asset and attribute node')
        counter = 0
        self.attributeListMainTab = []
        for control in self.controls.tabsWidgetListMain:
            log.debug('getting names for tab {}'.format(counter))
            removeRing = "{}.houdiniAssetParm_folder0[{}].houdiniAssetParm_removeRings_".format(self.jhumkaName, counter)
            log.debug('got the main remove ring parameter of the Houdini asset for the main section {} of the Jhumka: {} '.format(counter, removeRing))
            nodeOutRemoveRing = "{}.mainTabRemoveRing_{}".format(self.nodeName, counter)
            log.debug('got the main remove ring parameter of the attribute node for tab {}: {}'.format(counter, nodeOutRemoveRing))
            localList = [removeRing, nodeOutRemoveRing]
            self.attributeListMainTab.append(localList)
            log.debug('added Houdini and attribute node main remove ring parameter {} to attributeListMainTab'.format(counter))
            log.debug('houdini asset main remove ring checkbox {}  is - {} | node mainTabRemoveRing {} is {} | for jewlery {}'.format(counter, removeRing, counter, nodeOutRemoveRing, self.name))

            ringRadMain = "{}.houdiniAssetParm_folder0[{}].houdiniAssetParm_ringRadiusMain_".format(self.jhumkaName, counter)
            log.debug('got the main ring radius parameter of the Houdini asset for section {} of the Jhumka: {} '.format(counter, ringRadMain))
            nodeOutRingRadius = "{}.mainTabRingRadius_{}".format(self.nodeName, counter)
            log.debug('got the main ring radius parameter of the attribute node for tab {}: {}'.format(counter, nodeOutRingRadius))
            localList = [ringRadMain, nodeOutRingRadius]
            self.attributeListMainTab.append(localList)
            log.debug('added Houdini and attribute node main ring radius parameter {} to attributeListMainTab'.format(counter))
            log.debug('houdini asset main ring radius {}  is - {} | node mainTabRingRadius {} is {} | for jewlery {}'.format(counter, ringRadMain, counter, nodeOutRingRadius, self.name))
            #cmds.setAttr(hookScale, control.ringRadius.spinBox.value())
            

            detailType = "{}.houdiniAssetParm_folder0[{}].houdiniAssetParm_detailType_".format(self.jhumkaName, counter)
            log.debug('got the main detail type parameter of the Houdini asset for section {} of the Jhumka: {} '.format(counter, detailType))
            nodeOutDetailType = "{}.mainTabDetailType_{}".format(self.nodeName, counter)
            log.debug('got the main ring radius parameter of the attribute node for tab {}: {}'.format(counter, nodeOutDetailType))
            localList = [detailType, nodeOutDetailType]
            self.attributeListMainTab.append(localList)
            log.debug('added Houdini and attribute node main detail type parameter {}  to attributeListMainTab'.format(counter))
            log.debug('houdini asset main detail type {}  is - {} | node mainTabDetailType {} is {} | for jewlery {}'.format(counter, detailType, counter, nodeOutDetailType, self.name))
            

            repeatedDetail = "{}.houdiniAssetParm_folder0[{}].houdiniAssetParm_repeatedDetail_".format(self.jhumkaName, counter)
            log.debug('got the main repeated detail parameter of the Houdini asset for section {} of the Jhumka: {} '.format(counter, repeatedDetail))
            nodeOutRepeatedDetail = "{}.mainTabRepeatAmount_{}".format(self.nodeName, counter)
            log.debug('got the main repeated detail parameter of the attribute node for tab {}: {}'.format(counter, nodeOutRepeatedDetail))
            localList = [repeatedDetail, nodeOutRepeatedDetail]
            self.attributeListMainTab.append(localList)
            log.debug('added Houdini and attribute node main repeated detail parameter {} to attributeListMainTab'.format(counter))
            log.debug('houdini asset main repeated detail {}  is - {} | node mainTabRepeatedAmount {} is {} | for jewlery {}'.format(counter, repeatedDetail, counter, nodeOutRepeatedDetail, self.name))

            scaleMain = "{}.houdiniAssetParm_folder0[{}].houdiniAssetParm_scale_".format(self.jhumkaName, counter)
            log.debug('got the main scale parameter of the Houdini asset for section {} of the Jhumka: {} '.format(counter, scaleMain))
            nodeOutHookScale = "{}.mainTabScale_{}".format(self.nodeName, counter)
            log.debug('got the main scale parameter of the attribute node for tab {}: {}'.format(counter, nodeOutHookScale))
            localList = [scaleMain, nodeOutHookScale]
            self.attributeListMainTab.append(localList)
            log.debug('added Houdini and attribute node main scale parameter {} to attributeListMainTab'.format(counter))
            log.debug('houdini asset main scale {}  is - {} | node mainTabScape {} is {} | for jewlery {}'.format(counter, scaleMain, counter, nodeOutHookScale, self.name))
            #self.attributeListMainTab.append(localList)

            heightMain = "{}.houdiniAssetParm_folder0[{}].houdiniAssetParm_height_".format(self.jhumkaName, counter)
            log.debug('got the main height parameter of the Houdini asset for section {} of the Jhumka: {} '.format(counter, heightMain))
            nodeOutHeight = "{}.mainTabHeight_{}".format(self.nodeName, counter)
            log.debug('got the main height parameter of the attribute node for tab {}: {}'.format(counter, nodeOutHeight))
            localList = [heightMain, nodeOutHeight]
            self.attributeListMainTab.append(localList)
            log.debug('added Houdini and attribute node main height parameter {} to attributeListMainTab'.format(counter))
            log.debug('houdini asset main height {}  is - {} | node mainTabHeight {} is {} | for jewlery {}'.format(counter, heightMain, counter, nodeOutHeight, self.name))
            #self.attributeListMainTab.append(localList)

            depthMain = "{}.houdiniAssetParm_folder0[{}].houdiniAssetParm_depth_".format(self.jhumkaName, counter)
            log.debug('got the main depth parameter of the Houdini asset for section {} of the Jhumka: {} '.format(counter, depthMain))
            nodeOutDepth = "{}.mainTabDepth_{}".format(self.nodeName, counter)
            log.debug('got the main depth parameter of the attribute node for tab {}: {}'.format(counter, nodeOutDepth))
            localList = [depthMain, nodeOutDepth]
            self.attributeListMainTab.append(localList)
            log.debug('added Houdini and attribute node main depth parameter {} to attributeListMainTab'.format(counter))
            log.debug('houdini asset main depth {}  is - {} | node mainTabDepth {} is {} | for jewlery {}'.format(counter, depthMain, counter, nodeOutDepth, self.name))
            
            #self.attributeListMainTab.append(localList)

            rotationMain = "{}.houdiniAssetParm_folder0[{}].houdiniAssetParm_detailRotation_".format(self.jhumkaName, counter)
            log.debug('got the main detail rotation parameter of the Houdini asset for section {} of the Jhumka: {} '.format(counter, rotationMain))
            nodeOutRotation = "{}.mainTabRotation_{}".format(self.nodeName, counter)
            log.debug('got the main detail rotation parameter of the attribute node for tab {}: {}'.format(counter, nodeOutRotation))
            localList = [rotationMain, nodeOutRotation]
            self.attributeListMainTab.append(localList)
            log.debug('added Houdini and attribute node main detail rotation parameter {} to attributeListMainTab'.format(counter))
            log.debug('houdini asset main detail rotation {}  is - {} | node mainTabRotation {} is {} | for jewlery {}'.format(counter, rotationMain, counter, nodeOutRotation, self.name))
            #localList = [rotationMain, control.rotationSlider.spinBox]
            #self.attributeListMainTab.append(localList)
            
            fileSelector = "{}.houdiniAssetParm_folder0[{}].houdiniAssetParm_patternFile_".format(self.jhumkaName, counter)
            log.debug('got the main file selector parameter of the Houdini asset for section {} of the Jhumka: {} '.format(counter, fileSelector))
            nodeOutFileDir = "{}.mainFilePath_{}".format(self.nodeName, counter)
            log.debug('got the main file selector parameter of the attribute node for tab {}: {}'.format(counter, nodeOutFileDir))
            localList = [fileSelector, nodeOutFileDir]
            self.attributeListMainTab.append(localList)
            log.debug('added Houdini and attribute node main file selector parameter {} to attributeListMainTab'.format(counter))
            log.debug('houdini asset main file selector {}  is - {} | node mainFilePath {} is {} | for jewlery {}'.format(counter, fileSelector, counter, nodeOutFileDir, self.name))
            
            counter += 1

            
        #self.setupTabSignalSlots(self.attributeListMainTab)

    # def fileNameChanged(self, n, houVariable):
    #     log.debug('file name changed ')
    #     cmds.setAttr(houVariable, n, type = "string")


    def setupHookTab(self):
        log.debug('getting hook tab names for Houdini asset and attribute node')
        counter = 0
        #self.attributeListHookTab = []
        for control in self.controls.tabsWidgetListHook:
            log.debug('getting names for tab {}'.format(counter))

            ringRadMain = "{}.houdiniAssetParm_folder1[{}].houdiniAssetParm_ringRadiusHook_".format(self.jhumkaName, counter)
            log.debug('got the hook ring radius parameter of the Houdini asset for section {} of the Jhumka: {} '.format(counter, ringRadMain))
            nodeOutRingRadius = "{}.hookTabRingRadius_{}".format(self.nodeName, counter)
            log.debug('got the hook ring radius parameter of the attribute node for tab {}: {}'.format(counter, nodeOutRingRadius))
            localList = [ringRadMain, nodeOutRingRadius]
            self.attributeListMainTab.append(localList)
            log.debug('added Houdini and attribute node hook ring radius parameter {} to attributeListMainTab'.format(counter))
            log.debug('houdini asset hook ring radius {}  is - {} | node hookTabRingRadius {} is {} | for jewlery {}'.format(counter, ringRadMain, counter, nodeOutRingRadius, self.name))

            removeRing = "{}.houdiniAssetParm_folder1[{}].houdiniAssetParm_removeRingsCheck_".format(self.jhumkaName, counter)
            log.debug('got the hook remove ring parameter of the Houdini asset for the hook section {} of the Jhumka: {} '.format(counter, removeRing))
            nodeOutRemoveRing = "{}.hookTabRemoveRing_{}".format(self.nodeName, counter)
            log.debug('got the hook remove ring parameter of the attribute node for tab {}: {}'.format(counter, nodeOutRemoveRing))
            localList = [removeRing, nodeOutRemoveRing]
            self.attributeListMainTab.append(localList)
            log.debug('added Houdini and attribute node hook remove ring parameter {} to attributeListMainTab'.format(counter))
            log.debug('houdini asset hook remove ring checkbox {}  is - {} | node hookTabRemoveRing {} is {} | for jewlery {}'.format(counter, removeRing, counter, nodeOutRemoveRing, self.name))

            detailType = "{}.houdiniAssetParm_folder1[{}].houdiniAssetParm_detailTypeHook_".format(self.jhumkaName, counter)
            log.debug('got the hook detail type parameter of the Houdini asset for section {} of the Jhumka: {} '.format(counter, detailType))
            nodeOutDetailType = "{}.hookTabDetailType_{}".format(self.nodeName, counter)
            log.debug('got the hook ring radius parameter of the attribute node for tab {}: {}'.format(counter, nodeOutDetailType))
            localList = [detailType, nodeOutDetailType]
            self.attributeListMainTab.append(localList)
            log.debug('added Houdini and attribute node hook detail type parameter {}  to attributeListMainTab'.format(counter))
            log.debug('houdini asset hook detail type {}  is - {} | node hookTabDetailType {} is {} | for jewlery {}'.format(counter, detailType, counter, nodeOutDetailType, self.name))

            repeatedDetail = "{}.houdiniAssetParm_folder1[{}].houdiniAssetParm_repeatedDetailHook_".format(self.jhumkaName, counter)
            log.debug('got the hook repeated detail parameter of the Houdini asset for section {} of the Jhumka: {} '.format(counter, repeatedDetail))
            nodeOutRepeatedDetail = "{}.hookTabRepeatAmount_{}".format(self.nodeName, counter)
            log.debug('got the hook repeated detail parameter of the attribute node for tab {}: {}'.format(counter, nodeOutRepeatedDetail))
            localList = [repeatedDetail, nodeOutRepeatedDetail]
            self.attributeListMainTab.append(localList)
            log.debug('added Houdini and attribute node hook repeated detail parameter {} to attributeListMainTab'.format(counter))
            log.debug('houdini asset hook repeated detail {}  is - {} | node hookTabRepeatedAmount {} is {} | for jewlery {}'.format(counter, repeatedDetail, counter, nodeOutRepeatedDetail, self.name))

            scale = "{}.houdiniAssetParm_folder1[{}].houdiniAssetParm_scaleHook_".format(self.jhumkaName, counter)
            log.debug('got the hook scale parameter of the Houdini asset for section {} of the Jhumka: {} '.format(counter, scale))
            nodeOutHookScale = "{}.hookTabScale_{}".format(self.nodeName, counter)
            log.debug('got the hook scale parameter of the attribute node for tab {}: {}'.format(counter, nodeOutHookScale))
            localList = [scale, nodeOutHookScale]
            self.attributeListMainTab.append(localList)
            log.debug('added Houdini and attribute node hook scale parameter {} to attributeListMainTab'.format(counter))
            log.debug('houdini asset hook scale {}  is - {} | node hookTabScape {} is {} | for jewlery {}'.format(counter, scale, counter, nodeOutHookScale, self.name))
           


            height = "{}.houdiniAssetParm_folder1[{}].houdiniAssetParm_heightHook_".format(self.jhumkaName, counter)
            log.debug('got the hook height parameter of the Houdini asset for section {} of the Jhumka: {} '.format(counter, height))
            nodeOutHeight = "{}.hookTabHeight_{}".format(self.nodeName, counter)
            log.debug('got the hook height parameter of the attribute node for tab {}: {}'.format(counter, nodeOutHeight))
            localList = [height, nodeOutHeight]
            self.attributeListMainTab.append(localList)
            log.debug('added Houdini and attribute node hook height parameter {} to attributeListMainTab'.format(counter))
            log.debug('houdini asset hook height {}  is - {} | node hookTabHeight {} is {} | for jewlery {}'.format(counter, height, counter, nodeOutHeight, self.name))

            depth = "{}.houdiniAssetParm_folder1[{}].houdiniAssetParm_depthHook_".format(self.jhumkaName, counter)
            log.debug('got the depth depth parameter of the Houdini asset for section {} of the Jhumka: {} '.format(counter, depth))
            nodeOutDepth = "{}.hookTabDepth_{}".format(self.nodeName, counter)
            log.debug('got the hook depth parameter of the attribute node for tab {}: {}'.format(counter, nodeOutDepth))
            localList = [depth, nodeOutDepth]
            self.attributeListMainTab.append(localList)
            log.debug('added Houdini and attribute node hook depth parameter {} to attributeListMainTab'.format(counter))
            log.debug('houdini asset hook depth {}  is - {} | node hookTabDepth {} is {} | for jewlery {}'.format(counter, depth, counter, nodeOutDepth, self.name))
           

            detailRotation = "{}.houdiniAssetParm_folder1[{}].houdiniAssetParm_detailRotationHook_".format(self.jhumkaName, counter)
            log.debug('got the hook detail rotation parameter of the Houdini asset for section {} of the Jhumka: {} '.format(counter, detailRotation))
            nodeOutRotation = "{}.hookTabRotation_{}".format(self.nodeName, counter)
            log.debug('got the hook detail rotation parameter of the attribute node for tab {}: {}'.format(counter, nodeOutRotation))
            localList = [detailRotation, nodeOutRotation]
            self.attributeListMainTab.append(localList)
            log.debug('added Houdini and attribute node hook detail rotation parameter {} to attributeListMainTab'.format(counter))
            log.debug('houdini asset hook detail rotation {}  is - {} | node hookTabRotation {} is {} | for jewlery {}'.format(counter, detailRotation, counter, nodeOutRotation, self.name))

            fileSelector = "{}.houdiniAssetParm_folder1[{}].houdiniAssetParm_patternFileHook_".format(self.jhumkaName, counter)
            log.debug('got the hook file selector parameter of the Houdini asset for section {} of the Jhumka: {} '.format(counter, fileSelector))
            nodeOutFileDir = "{}.hookFilePath_{}".format(self.nodeName, counter)
            log.debug('got the hook file selector parameter of the attribute node for tab {}: {}'.format(counter, nodeOutFileDir))
            localList = [fileSelector, nodeOutFileDir]
            self.attributeListMainTab.append(localList)
            log.debug('added Houdini and attribute node hook file selector parameter {} to attributeListMainTab'.format(counter))
            log.debug('houdini asset hook file selector {}  is - {} | node hookFilePath {} is {} | for jewlery {}'.format(counter, fileSelector, counter, nodeOutFileDir, self.name))

            counter += 1

   

    # def setComboIndex(self, houVariable, n):
    #     cmds.setAttr(houVariable, n)

    # def checkboxChecked(self, houVariable, n):
    #     if(n == 2):
    #         cmds.setAttr(houVariable, 1)

    #     else:
    #         cmds.setAttr(houVariable, 0)


    def setupTabSignalSlots(self, list):
        log.debug("Setting up signals and slots")
        for each in list:
            log.debug("connecting {} to {}".format(each[1], each[0]))

            try:
                cmds.connectAttr( each[1], each[0], f=1)
                log.info("connected {} to {}".format(each[1], each[0]))

            except Exception as e:
                log.debug("can't connect {} to {}, exception: {}".format(each[1], each[0], e))





    # def slot(self, n, houVariable):
    #     cmds.connectAttr(houVariable, n)
    #     connectAttr -f tes_JhumkaAttributesNode.outRows tes_Jhumka.houdiniAssetParm_jhumka_Rows