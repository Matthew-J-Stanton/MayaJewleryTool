import logging
import os

#logging.basicConfig()
log = logging.getLogger("Jewlery Tool")
fileName = os.path.splitext(os.path.basename(__file__))[0]


log.debug('{} loading'.format(fileName))
try:
    log.debug('trying to import PySide 2 into {}'.format(fileName))
    from PySide2.QtCore import *
    from PySide2.QtGui import *
    from PySide2.QtWidgets import *
    # So we import wrapInstance from sip and alias it to wrapInstance so that it's the same as the others
    from shiboken2 import wrapInstance
    log.debug('Using PySide2 and Shiboken2 into {}'.format(fileName))


except:
    log.debug('PySide 2 not avalable')
    try:
        log.debug('trying to import PySide into {}'.format(fileName))
        from PySide.QtCore import *
        from PySide.QtGui import *
        from PySide.QtWidgets import *
        # So we import wrapInstance from sip and alias it to wrapInstance so that it's the same as the others
        from shiboken import wrapinstance 
        log.debug('Using PySide and Shiboken into {}'.format(fileName))


    except:
        log.debug('Pyside not avalable')
        try:
            log.debug('trying to import PyQt5 into {}'.format(fileName))
            from PyQt5.QtCore import *
            from PyQt5.QtGui import *
            from PyQt5.QtWidgets import *
            # So we import wrapInstance from sip and alias it to wrapInstance so that it's the same as the others
            from sip import wrapinstance as wrapInstance
            log.debug('Using PyQt5 and sip into {}'.format(fileName))

        except:
            log.debug('PyQt5 not avalable')
            log.debug('trying to import PyQt4 into {}'.format(fileName))
            from PyQt4.QtCore import *
            from PyQt4.QtGui import *
            from PyQt4.QtWidgets import *
            # So we import wrapInstance from sip and alias it to wrapInstance so that it's the same as the others
            from sip import wrapinstance as wrapInstance
            log.debug('Using PyQt4 and sip into {}'.format(fileName))


import pymel.core as pm
log.debug('imported pymel.core')

import maya.cmds as cmds
log.debug('imported maya.cmds')

from maya import OpenMayaUI as omui
log.debug('imported OpenMayaUI')

import maya.api.OpenMaya as om
log.debug('imported OpenMaya')

import time
log.debug('imported time')

import sys

from tabWidget import createMainJhumkaTabWidget
log.debug('imported createMainJhumkaTabWidget')

from Jhumka import jhumka
log.debug('imported jhumka')

from createVariableSlider import createVariableSlider
log.debug('imported createVariableSlider')

log.info("Imported libraries into {}".format(fileName))

plugin_root = os.environ.get("JEWLERYTOOLPLUGIN_ROOT")

imageFilesPath = plugin_root + "/image-files/"

def deleteDock(name="controls_dock"):
    log.info("checking if dock exsists")
    if pm.workspaceControl(name, query=True, exists=True):
        log.info("dock exsists")
        log.info("deleting dock")
        pm.workspaceControl(name, e=True, close=True)
        log.info("dock deleted")

    else:
        log.info("dock doesn't exsist")

def reopenDock(name):
    log.info("dock reopening")

    log.debug("checking if {} dock exists".format(name))
    if pm.workspaceControl(name, query=True, exists=True):
        log.debug("dock {} exists".format(name))
        log.info("restoring {} dock".format(name))
        pm.workspaceControl(name, edit=True, restore=True)
        log.info("{} dock restored".format(name))
        return 1
    else:
        return 0


def createDock(name, rebuild, dialog_class):
    isReopened = 0
    log.debug("checking if {} dock is new or being reopened".format(name))
    if( rebuild ):
        log.debug("{} dock is being reopened".format(name))
        log.debug("checking if {} dock needs to be rebuilt or is already open".format(name))
        isReopened = reopenDock(name)
    else:
        log.debug("{} dock is not being reopened".format(name))


    log.info("---Creating Dock---")
    
    

    if not isReopened:
        log.debug("{} dock needs to be built".format(name))

        log.debug("checking if {} dock is new or being reopened".format(name))
        if not rebuild:
            log.info("{} dock is new".format(name))
            log.debug("Creating {} Node".format(name))
            attrNode = cmds.createNode("AttributeNode")
            log.info("{} node created as {}".format(name, attrNode))

        
            
            log.debug("renaming {} node to {}_JhumkaAttributesNode".format(name, name))
            pm.rename( attrNode, name+"_JhumkaAttributesNode" )
            log.info("node renamed to {}".format(name))
        

        tabname = name + " controls"
        log.debug("created tabname as {}".format(tabname))

        log.debug("setting up dock control for {}".format(tabname))

        main_control = pm.workspaceControl(name, ttc=["AttributeEditor", -1], label=tabname)

        control_widget = omui.MQtUtil.findControl(name)

        control_wrap = wrapInstance(long(control_widget), QWidget)

        log.debug("created dock control for {}".format(tabname))
        
        win = dialog_class(control_wrap, name, rebuild)
        
        pm.evalDeferred(lambda *args:cmds.workspaceControl(main_control, iw = 325, mw = 1, wp = 'fixed',e=True, rs=True, rt=0))
        
        log.info("dock {} set up".format(tabname))

        return win
    



class controls(QWidget):



    
    def __init__(self, parent=None, name = "Jhumka", rebuild=0):

        log.debug("initializing {} dock widget".format(name))
        
        self.Jhumka = None
        self.name = name
        self.nodeName = "{}_JhumkaAttributesNode".format(name)
        self.tabsWidgetListMain = []
        self.tabsWidgetListHook = []
        log.debug("setup {} dock widget lists".format(name))
        
        self.window_name = 'Test'
        #parent.setObjectName('lightingManager')

        #deleteDock()
           
        if sys.version_info.major == 3:
            super().__init__()
        # python 2
        else:
            super(controls, self).__init__(parent)
        
        self.ui = parent
        self.main_layout = parent.layout()
        
        self.setupUi(self, rebuild)
        
        

        
        
    # def run(self):
    #     return self

    def setupUi(self, Form, rebuild):
        log.debug("setup {} dock UI".format(self.name))
            
        self.attributeList = []
        self.rebuild = rebuild

        if not Form.objectName():
    
            Form.setObjectName(u"Form")
        Form.resize(323, 700)
        #self.widget1 = QWidget(self)

        layout = QVBoxLayout()
       
        self.scrollAreaMain = QScrollArea(Form)
        self.scrollAreaMain.setObjectName("scrollAreaMain")
        self.scrollAreaMain.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -146, 245, 253))
        self.scrollAreaMain.setMaximumHeight(700)
        self.scrollAreaMain.setMinimumHeight(650)
        
        layout.addWidget(self.scrollAreaMain)
        self.scrollAreaMain.setWidget(self.scrollAreaWidgetContents)
        self.scrollAreaMain.setFrameShape(QFrame.NoFrame)
        #self.scrollLayoutMain.setContentsMargins(0, 0 ,0 , 0)
        self.scrollAreaMain.setContentsMargins(0, 0 ,0 , 0)

        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        
        self.jhumkaRowsSlider = createVariableSlider("Rows", 50, 100, 1, single_step=1)
        self.gridLayout.addWidget(self.jhumkaRowsSlider, 0, 0, 1, 1)
        nodeAttr = "{}.rows".format(self.nodeName)
        log.debug('got the rows parameter of the attribute node for jewlery {}: {}'.format(self.name, nodeAttr))
        localList = [nodeAttr, self.jhumkaRowsSlider.spinBox]
        self.attributeList.append(localList)
        log.debug('added controls slider and node attribute rows parameter to attributeList')
        

        self.jhumkaColumnsSlider = createVariableSlider("Columns", 27, 100, 1, single_step=1)
        self.gridLayout.addWidget(self.jhumkaColumnsSlider, 1, 0, 1, 1)
        nodeAttr = "{}.columns".format(self.nodeName)
        log.debug('got the columns  parameter of the attribute node for jewlery {}: {}'.format(self.name, nodeAttr))
        localList = [nodeAttr, self.jhumkaColumnsSlider.spinBox]
        self.attributeList.append(localList)
        log.debug('added controls slider and node attribute columns parameter to attributeList')
       
        self.jhumkaScaleSlider = createVariableSlider("Scale", 1.5, 5, 0, single_step=0.05)
        self.gridLayout.addWidget(self.jhumkaScaleSlider, 2, 0, 1, 1)
        nodeAttr = "{}.scale".format(self.nodeName)
        log.debug('got the scale parameter of the attribute node for jewlery {}: {}'.format(self.name, nodeAttr))
        localList = [nodeAttr, self.jhumkaScaleSlider.spinBox]
        self.attributeList.append(localList)
        log.debug('added controls slider and node attribute scale parameter to attributeList')
        
        self.jhumkaStretchSlider = createVariableSlider("Stretch", 1.15, 5, 0 ,single_step=0.05)
        self.gridLayout.addWidget(self.jhumkaStretchSlider, 3, 0, 1, 1)
        nodeAttr = "{}.stretch".format(self.nodeName)
        log.debug('got the stretch parameter of the attribute node for jewlery {}: {}'.format(self.name, nodeAttr))
        localList = [nodeAttr, self.jhumkaStretchSlider.spinBox]
        self.attributeList.append(localList)
        log.debug('added controls slider and node attribute stretch parameter to attributeList')

        self.jhumkaAmountSlider = createVariableSlider("Jhumka Amount", 10, 20, 1 ,single_step=1)
        self.gridLayout.addWidget(self.jhumkaAmountSlider, 4, 0, 1, 1)
        self.jhumkaAmountSlider.slider.valueChanged.connect(lambda val : self.numMainSectionsChanged(val))
        nodeAttr = "{}.jhumkaAmount".format(self.nodeName)
        log.debug('got the amount parameter of the attribute node for jewlery {}: {}'.format(self.name, nodeAttr))
        localList = [nodeAttr, self.jhumkaAmountSlider.spinBox]
        self.attributeList.append(localList)
        log.debug('added controls slider and node attribute amount parameter to attributeList')

        self.dangleSizeSlider = createVariableSlider("Dangle size", 1, 5, 0 ,single_step=0.05)
        self.gridLayout.addWidget(self.dangleSizeSlider, 5, 0, 1, 1)
        nodeAttr = "{}.dangleSize".format(self.nodeName)
        log.debug('got the dangle size parameter of the attribute node for jewlery {}: {}'.format(self.name, nodeAttr))
        localList = [nodeAttr, self.dangleSizeSlider.spinBox]
        self.attributeList.append(localList)
        log.debug('added controls slider and node attribute dangle size parameter to attributeList')
        

        self.tabWidget = QTabWidget(Form)
        
        self.tabWidget.setObjectName(u"tabWidget")
        self.mainTab = QWidget()
        self.mainTab.setObjectName(u"mainTab")
        self.verticalLayout = QVBoxLayout(self.mainTab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        

       

        self.maiJhumka_tabs = QTabWidget(self.mainTab)
        self.maiJhumka_tabs.setContentsMargins(0, 0 ,0 , 0)
        self.maiJhumka_tabs.setObjectName(u"maiJhumka_tabs")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.maiJhumka_tabs.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.maiJhumka_tabs.addTab(self.tab_2, "")

        

        self.verticalLayout.addWidget(self.maiJhumka_tabs)

        self.tabWidget.addTab(self.mainTab, "")
        self.hookTab = QWidget()
        self.hookTab.setObjectName(u"hookTab")
        self.gridLayout_2 = QGridLayout(self.hookTab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.numberOfSectionsSlider = createVariableSlider("Number of Sections", 6, 10, 1 ,single_step=1)
        self.gridLayout_2.addWidget(self.numberOfSectionsSlider, 1, 0, 1, 1)
        self.numberOfSectionsSlider.slider.valueChanged.connect(self.numHookSectionsChanged)
        nodeAttr = "{}.numOfSec".format(self.nodeName)
        log.debug('got the number of hook sections parameter of the attribute node for jewlery {}: {}'.format(self.name, nodeAttr))
        localList = [nodeAttr, self.numberOfSectionsSlider.spinBox]
        self.attributeList.append(localList)

        self.jewelSizeSlider = createVariableSlider("Jewel Size", 1, 6, 1 ,single_step=1)
        self.gridLayout_2.addWidget(self.jewelSizeSlider, 0, 0, 1, 1)
        self.jewelSizeSlider.slider.valueChanged.connect(self.numHookSectionsChanged)
        nodeAttr = "{}.jewelSize".format(self.nodeName)
        log.debug('got the jewel size parameter of the attribute node for jewlery {}: {}'.format(self.name, nodeAttr))
        localList = [nodeAttr, self.jewelSizeSlider.spinBox]
        self.attributeList.append(localList)

        self.hookScaleSlider = createVariableSlider("Hook Circle Scale", 0.980, 10, 0 ,single_step=0.05)
        self.gridLayout_2.addWidget(self.hookScaleSlider, 3, 0, 1, 1)
        nodeAttr = "{}.HookCircleRadius".format(self.nodeName)
        log.debug('got the hook scale parameter of the attribute node for jewlery {}: {}'.format(self.name, nodeAttr))
        localList = [nodeAttr, self.hookScaleSlider.spinBox]
        self.attributeList.append(localList)

        
        self.jhumkaHookTabs = QTabWidget(self.hookTab)
        self.jhumkaHookTabs.setObjectName(u"jhumkaHookTabs")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.jhumkaHookTabs.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.jhumkaHookTabs.addTab(self.tab_4, "")
        self.tabWidget.currentChanged.connect(lambda n: self.tabChanged(n))

        self.gridLayout_2.addWidget(self.jhumkaHookTabs, 4, 0, 1, 3)

        self.tabWidget.addTab(self.hookTab, "")

        self.gridLayout.addWidget(self.tabWidget, 7, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 28, QSizePolicy.Maximum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 9, 0, 1, 1)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)
        
        self.blendCheckBox = QCheckBox("Blend Chumka")
        self.gridLayout.addWidget(self.blendCheckBox, 8, 0, 1, 1)
        nodeAttr = "{}.BlendJhumka".format(self.nodeName)
        log.debug('got the blend checkbox parameter of the attribute node for jewlery {}: {}'.format(self.name, nodeAttr))
        self.blendCheckBox.stateChanged.connect(lambda n : self.checkboxChecked(n, nodeAttr))

        self.messageLineEdit = QLineEdit()
        self.messageLineEdit.setReadOnly(True)
        self.gridLayout.addWidget(self.messageLineEdit, 9, 0, 1, 1)

        self.createBttn = QPushButton("Create")
        self.createBttn.clicked.connect(lambda: self.create())
        self.gridLayout.addWidget(self.createBttn, 9, 1, 1, 1)
        self.numMainSectionsChanged(10)
        #self.tabWidget.setCurrentIndex(1)
        
        self.tabWidget.setMaximumHeight(100)
        self.tabWidget.setMinimumHeight(100)
        self.maiJhumka_tabs.setMaximumHeight(500)
        self.jhumkaHookTabs.setMaximumHeight(100)

        self.tabWidget.blockSignals(False)
        
        self.numHookSectionsChanged()
        QMetaObject.connectSlotsByName(Form)

        log.debug('checking if the attributes need to be rebuilt for jewlery {}'.format(self.name))
        if(rebuild):
            log.info('attributes need to be rebuilt for jewlery {}'.format(self.name))
            self.rebuildAttributes()

        self.setupSignalsAndSlots()
        #self.setupSignalsSlots()
    setupUi

    def tabChanged(self, n):
        log.debug('Tab changed function run for controls of {}'.format(self.name))

        log.debug('Checking which tab has been changed to:')
        if( n ==  0):
            log.debug('{} tab changed to main jhumka tab'.format(self.name))
            log.debug('{} tab changing height to 100'.format(self.name))
            self.jhumkaHookTabs.setMaximumHeight(100)
            log.debug('{} tab changed height to 100'.format(self.name))
        if( n == 1):
            log.debug('{} tab changed to hook jhumka tab'.format(self.name))
            log.debug('{} tab changing height to 500'.format(self.name))
            self.jhumkaHookTabs.setMaximumHeight(500)
            log.debug('{} tab changed height to 500'.format(self.name))

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.maiJhumka_tabs.setTabText(self.maiJhumka_tabs.indexOf(self.tab), QCoreApplication.translate("Form", u"Tab 1", None))
        self.maiJhumka_tabs.setTabText(self.maiJhumka_tabs.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Tab 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mainTab), QCoreApplication.translate("Form", u"Main Jhumka", None))
        
        self.jhumkaHookTabs.setTabText(self.jhumkaHookTabs.indexOf(self.tab_3), QCoreApplication.translate("Form", u"Tab 1", None))
        self.jhumkaHookTabs.setTabText(self.jhumkaHookTabs.indexOf(self.tab_4), QCoreApplication.translate("Form", u"Tab 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.hookTab), QCoreApplication.translate("Form", u"Jhumka Hook", None))
        
    # retranslateUi


    def setupSignalsAndSlots(self):
        log.info('setting up signals and slots for {}'.format(self.name))
        for each in self.attributeList:
            log.debug('connecting the changing of variable {} to change {}'.format(each[1], each[0]))
            each[1].valueChanged.connect(lambda n, nodeVariable = each[0]: self.slot(n, nodeVariable))
            log.debug('connected the changing of variable {} to change {}'.format(each[1], each[0]))

    def slot(self, n, nodeVariable):
        strNodeVariable = str(nodeVariable)
        log.debug("setting {} to {}".format(nodeVariable, n))
        cmds.setAttr(nodeVariable, n)
        log.info("set {} to {}".format(nodeVariable, n))
    


    def showText(self, text):
        log.info('showing text {} in message line edit of {}'.format(text, self.name))
        self.messageLineEdit.setText(text)
        log.debug('showed text')
        self.messageLineEdit.repaint()
        







    def create(self):
        
        # print("test1")

        log.info('create function run for controls {}'.format(self.name))

        self.showText("Creating Jhumka...")
        
        log.debug('running Jhumka function')
        self.Jhumka = jhumka(self, self.name)
        
        
        self.showText("Jhumka Created")
        log.info('{} Jhumka created'.format(self.name))
        time.sleep(1)
        self.showText("")

    def numMainSectionsChanged(self, n):
        log.info('number of main sections changed for jhumka {}'.format(self.name))
        self.maiJhumka_tabs.clear()
        log.debug('{} main tabs cleared'.format(self.name))
        self.tabsWidgetListMain = []
        n = n-1

        log.info('loop for {} to create {}  main tabs'.format(self.name, n))
        for section in range(0, n):
            section = section + 1

            self.tab=QWidget()

            tabName = "Tab %s"%section

            self.maiJhumka_tabs.addTab(self.tab, tabName)


            self.tab.layout = QVBoxLayout(self.tab)
            self.tabWidget = createMainJhumkaTabWidget("Widget")
            self.tabsWidgetListMain.append(self.tabWidget)
            self.tab.layout.addWidget(self.tabWidget)
            nodeAttrFilePath = "{}.{}FilePath_{}".format(self.nodeName, "main", section-1)
            pattern = "{}pattern.png".format(imageFilesPath)
            cmds.setAttr( nodeAttrFilePath , pattern, type="string")
            log.debug('setAttr {} as {}'.format( nodeAttrFilePath , pattern))

            
            self.rebuildTabAttibutes(section-1, self.tabWidget, "main")

            self.setupTabSignalAndSlotMain(section-1, self.tabWidget)
            if(self.Jhumka):
                self.Jhumka.setupMainTab()
                self.Jhumka.setupTabSignalSlots(self.Jhumka.attributeListMainTab)

    def setupTabSignalAndSlotMain(self, num, tabWidget):
        
        

        nodeAttrRemoveRing = "{}.mainTabRemoveRing_{}".format(self.nodeName, num)
        log.debug('remove ring {} parameter found as {} for attribute node in main tab of controls {}'.format( num, nodeAttrRemoveRing ,self.name))
        tabWidget.checkBox.stateChanged.connect(lambda n: self.checkboxChecked(n, nodeAttrRemoveRing))
        log.debug('connected remove ring {} checkbox to checkboxChecked function in main tab of controls {}'.format(num, self.name))
        
        nodeAttrScale = "{}.mainTabScale_{}".format(self.nodeName, num)
        log.debug('scale {} parameter found as {} for attribute node in main tab of controls {}'.format( num, nodeAttrScale ,self.name))
        tabWidget.scaleSlider.spinBox.valueChanged.connect(lambda n: self.slot(n, nodeAttrScale))
        log.debug('connected scale {} spinbox to slot function in main tab of controls {}'.format(num, self.name))

        nodeAttrDetailType = "{}.mainTabDetailType_{}".format(self.nodeName, num)
        log.debug('detail type {} parameter found as {} for attribute node in main tab of controls {}'.format( num, nodeAttrDetailType ,self.name))
        tabWidget.comboBox.currentIndexChanged.connect(lambda n: self.slot(n, nodeAttrDetailType))
        log.debug('connected detail type {} combo box to slot function in main tab of controls {}'.format(num, self.name))
        
        nodeAttrRingRadius = "{}.mainTabRingRadius_{}".format(self.nodeName, num)
        log.debug('ring radius {} parameter found as {} for attribute node in main tab of controls {}'.format(num, nodeAttrRingRadius ,self.name))
        tabWidget.ringRadius.spinBox.valueChanged.connect(lambda n: self.slot(n, nodeAttrRingRadius))
        log.debug('connected ring radius {} spin box to slot function in main tab of controls {}'.format(num, self.name))

        nodeAttrRepeatAmount = "{}.mainTabRepeatAmount_{}".format(self.nodeName, num)
        log.debug('repeat amount {} parameter found as {} for attribute node in main tab of controls {}'.format( num, nodeAttrRepeatAmount ,self.name))
        tabWidget.repeatedDetailSlider.spinBox.valueChanged.connect(lambda n: self.slot(n, nodeAttrRepeatAmount))
        log.debug('connected repeat amount {} spinbox to slot function in main tab of controls {}'.format(num, self.name))

        nodeAttrHeight = "{}.mainTabHeight_{}".format(self.nodeName, num)
        log.debug('height {} parameter found as {} for attribute node in main tab of controls {}'.format( num, nodeAttrHeight ,self.name))
        tabWidget.heightSlider.spinBox.valueChanged.connect(lambda n: self.slot(n, nodeAttrHeight))
        log.debug('connected height {} spinbox to slot function in main tab of controls {}'.format(num, self.name))

        nodeAttrDepth = "{}.mainTabDepth_{}".format(self.nodeName, num)
        log.debug('depth {} parameter found as {} for attribute node in main tab of controls {}'.format( num, nodeAttrDepth ,self.name))
        tabWidget.depthSlider.spinBox.valueChanged.connect(lambda n: self.slot(n, nodeAttrDepth))
        log.debug('connected depth {} spinbox to slot function in main tab of controls {}'.format(num, self.name))

        nodeAttrRotation = "{}.mainTabRotation_{}".format(self.nodeName, num)
        log.debug('rotation {} parameter found as {} for attribute node in main tab of controls {}'.format( num, nodeAttrRotation ,self.name))
        tabWidget.rotationSlider.spinBox.valueChanged.connect(lambda n: self.slot(n, nodeAttrRotation))
        log.debug('connected detail rotation {} spinbox to slot function in main tab of controls {}'.format(num, self.name))

        nodeAttrFilePath = "{}.mainFilePath_{}".format(self.nodeName, num)
        log.debug('file path {} parameter found as {} for attribute node in main tab of controls {}'.format( num, nodeAttrFilePath ,self.name))
        tabWidget.fileSelector.fileNameLineEdit.textChanged.connect(lambda n: self.slotString(n, nodeAttrFilePath))
        log.debug('connected file line edit {} to slotString function in main tab of controls {}'.format(num, self.name))


    


    def numHookSectionsChanged(self):
        log.info('number of hook sections changed for jhumka {}'.format(self.name))
        self.jhumkaHookTabs.clear()
        log.debug('{} hook tabs cleared'.format(self.name))
        self.tabsWidgetListHook = []
        jewelSize = self.jewelSizeSlider.slider.value()
        n = self.numberOfSectionsSlider.slider.value()
        numOfSections = n - jewelSize - 1

        log.info('loop for {} to create {} hook tabs'.format(self.name, n))
        for section in range(0, numOfSections):
            section = section + 1

            self.tab=QWidget()

            tabName = "Tab %s"%section

            self.jhumkaHookTabs.addTab(self.tab, tabName)


            self.tab.layout = QVBoxLayout(self.tab)
            self.tabWidget = createMainJhumkaTabWidget("Widget")
            self.tabsWidgetListHook.append(self.tabWidget)
            
            self.tab.layout.addWidget(self.tabWidget)

            nodeAttrFilePath = "{}.{}FilePath_{}".format(self.nodeName, "hook", section-1)
            pattern = "{}pattern.png".format(imageFilesPath)
            cmds.setAttr( nodeAttrFilePath , pattern, type="string")
            log.warning('setAttr {} as {}'.format( nodeAttrFilePath , pattern))
            
            self.rebuildTabAttibutes(section-1, self.tabWidget, "hook")

            self.setupTabSignalAndSlotHook(section-1, self.tabWidget)

    def setupTabSignalAndSlotHook(self, num, tabWidget):

        nodeAttrRemoveRing = "{}.hookTabRemoveRing_{}".format(self.nodeName, num)
        log.debug('remove ring parameter found as {} for attribute node in hook tab of controls {}'.format( nodeAttrRemoveRing ,self.name))
        tabWidget.checkBox.stateChanged.connect(lambda n: self.checkboxChecked(n, nodeAttrRemoveRing))
        log.debug('connected remove ring {} checkbox to checkboxChecked function in hook tab of controls {}'.format(num, self.name))

        nodeAttrScale = "{}.hookTabScale_{}".format(self.nodeName, num)
        log.debug('scale parameter found as {} for attribute node in hook tab of controls {}'.format( nodeAttrScale ,self.name))
        tabWidget.scaleSlider.spinBox.valueChanged.connect(lambda n: self.slot(n, nodeAttrScale))
        log.debug('connected scale {} spinbox to slot function in hook tab of controls {}'.format(num, self.name))
        
        nodeAttrRingRadius = "{}.hookTabRingRadius_{}".format(self.nodeName, num)
        log.debug('ring radius parameter found as {} for attribute node in hook tab of controls {}'.format( nodeAttrRingRadius ,self.name))
        tabWidget.ringRadius.spinBox.valueChanged.connect(lambda n: self.slot(n, nodeAttrRingRadius))
        log.debug('connected ring radius {} spin box to slot function in hook tab of controls {}'.format(num, self.name))

        nodeAttrDetailType = "{}.hookTabDetailType_{}".format(self.nodeName, num)
        log.debug('detail type parameter found as {} for attribute node in hook tab of controls {}'.format( nodeAttrDetailType ,self.name))
        tabWidget.comboBox.currentIndexChanged.connect(lambda n: self.slot(n, nodeAttrDetailType))
        log.debug('connected detail type {} combo box to slot function in hook tab of controls {}'.format(num, self.name))

        nodeAttrRepeatAmount = "{}.hookTabRepeatAmount_{}".format(self.nodeName, num)
        log.debug('repeat amount parameter found as {} for attribute node in hook tab of controls {}'.format( nodeAttrRepeatAmount ,self.name))
        tabWidget.repeatedDetailSlider.spinBox.valueChanged.connect(lambda n: self.slot(n, nodeAttrRepeatAmount))
        log.debug('connected repeat amount {} spinbox to slot function in hook tab of controls {}'.format(num, self.name))

        nodeAttrHeight = "{}.hookTabHeight_{}".format(self.nodeName, num)
        log.debug('height parameter found as {} for attribute node in hook tab of controls {}'.format( nodeAttrHeight ,self.name))
        tabWidget.heightSlider.spinBox.valueChanged.connect(lambda n: self.slot(n, nodeAttrHeight))
        log.debug('connected height {} spinbox to slot function in hook tab of controls {}'.format(num, self.name))

        nodeAttrDepth = "{}.hookTabDepth_{}".format(self.nodeName, num)
        log.debug('depth parameter found as {} for attribute node in hook tab of controls {}'.format( nodeAttrDepth ,self.name))
        tabWidget.depthSlider.spinBox.valueChanged.connect(lambda n: self.slot(n, nodeAttrDepth))
        log.debug('connected depth {} spinbox to slot function in hook tab of controls {}'.format(num, self.name))

        nodeAttrRotation = "{}.hookTabRotation_{}".format(self.nodeName, num)
        log.debug('detail rotation parameter found as {} for attribute node in hook tab of controls {}'.format( nodeAttrRotation ,self.name))
        tabWidget.rotationSlider.spinBox.valueChanged.connect(lambda n: self.slot(n, nodeAttrRotation))
        log.debug('connected detail rotation {} spinbox to slot function in hook tab of controls {}'.format(num, self.name))
        

        nodeAttrFilePath = "{}.hookFilePath_{}".format(self.nodeName, num)
        log.debug('file path parameter found as {} for attribute node in hook tab of controls {}'.format( nodeAttrFilePath ,self.name))
        tabWidget.fileSelector.fileNameLineEdit.textChanged.connect(lambda n: self.slotString(n, nodeAttrFilePath))
        log.debug('connected file line edit {} to slotString function in hook tab of controls {}'.format(num, self.name))

    def checkboxChecked(self, n, nodeAttr):
        if(n == 2):
            log.debug('checkbox checked in controls {}, setting attribute {} to 1'.format(self.name, nodeAttr))
            cmds.setAttr( nodeAttr , 1)
            log.info('set attribute {} to 1'.format(nodeAttr))

        else:
            log.debug('checkbox unchecked checked in controls {}, setting attribute {} to 0'.format(self.name, nodeAttr))
            cmds.setAttr( nodeAttr , 0)
            log.info('set attribute {} to 0'.format(nodeAttr))

    # def setAttribute(self, n, nodeAttr):
    
    #     cmds.setAttr( nodeAttr , n)

    def slotString(self, n, nodeAttr):
        log.debug('line edit value changed setting {} to {}'.format(nodeAttr, n))
        cmds.setAttr( nodeAttr , n, type="string")
        log.info('set {} to {}'.format(nodeAttr, n))

    def rebuildAttributes(self):
        log.info('rebuilding attributes for {}'.format(self.name))
        for each in self.attributeList:
            value = pm.getAttr(each[0])

            log.debug('setting {} to reloaded value {}'.format(each[1], value))
            each[1].setValue(value)
            log.info('set {} to reloaded value {}'.format(each[1], value))
            
            #cmds.setAttr(each[0], each[1])

    def rebuildTabAttibutes(self, num, tabWidget, section):
        log.info('reloading {} tab {} attributes for {}'.format(section, num, self.name))
        nodeAttrRemoveRing = "{}.{}TabRemoveRing_{}".format(self.nodeName, section, num)
        val = bool(pm.getAttr(nodeAttrRemoveRing))
        tabWidget.checkBox.setChecked(val)
        log.info('set {} {} remove ring checkbox to reloaded value {}'.format(self.name, section, pm.getAttr( nodeAttrRemoveRing)))

        nodeAttrScale = "{}.{}TabScale_{}".format(self.nodeName, section ,num)
        tabWidget.scaleSlider.spinBox.setValue(pm.getAttr(nodeAttrScale))
        log.info('set {} {} scale spin box to reloaded value {}'.format(self.name, section, pm.getAttr( nodeAttrScale)))

        
        nodeAttrRingRadius = "{}.{}TabRingRadius_{}".format(self.nodeName, section, num)
        tabWidget.ringRadius.spinBox.setValue(pm.getAttr(nodeAttrRingRadius))
        log.info('set {} {} ring radius spin box to reloaded value {}'.format(self.name, section, pm.getAttr( nodeAttrRingRadius)))

        

        nodeAttrDetailType = "{}.{}TabDetailType_{}".format(self.nodeName, section, num)
        tabWidget.comboBox.setCurrentIndex(pm.getAttr(nodeAttrDetailType))
        log.info('set {} {} detail type combo box index to reloaded value {}'.format(self.name, section, pm.getAttr( nodeAttrDetailType)))

        nodeAttrRepeatAmount = "{}.{}TabRepeatAmount_{}".format(self.nodeName, section, num)
        tabWidget.repeatedDetailSlider.spinBox.setValue(pm.getAttr(nodeAttrRepeatAmount))
        log.info('set {} {} repeat amount spin box to reloaded value {}'.format(self.name, section, pm.getAttr( nodeAttrRepeatAmount)))

        nodeAttrHeight = "{}.{}TabHeight_{}".format(self.nodeName, section, num)
        tabWidget.heightSlider.spinBox.setValue(pm.getAttr(nodeAttrHeight))
        log.info('set {} {} height spinbox to reloaded value {}'.format(self.name, section, pm.getAttr( nodeAttrHeight )))
        

        nodeAttrDepth = "{}.{}TabDepth_{}".format(self.nodeName, section, num)
        tabWidget.depthSlider.spinBox.setValue(pm.getAttr(nodeAttrDepth))
        log.info('set {} {} depth spinbox to reloaded value {}'.format(self.name, section, pm.getAttr( nodeAttrDepth)))
        

        nodeAttrRotation = "{}.{}TabRotation_{}".format(self.nodeName, section, num)
        tabWidget.rotationSlider.spinBox.setValue(pm.getAttr(nodeAttrRotation))
        log.info('set {} {} detail rotation spinbox to reloaded value {}'.format(self.name, section, pm.getAttr( nodeAttrRotation)))
        

        nodeAttrFilePath = "{}.{}FilePath_{}".format(self.nodeName, section, num)
        filePath = pm.getAttr( nodeAttrFilePath)
        
        tabWidget.fileSelector.fileNameLineEdit.setText(filePath)
        
        
        log.info('set {} {} file path line edit to reloaded value {}'.format(self.name, section,filePath ))
        




class createControls():
    
    def __init__(self, main_window, name, rebuild=0):
        main_window.showMinimized()
        my_dock = createDock(name, rebuild, controls)



