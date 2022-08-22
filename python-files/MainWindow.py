import os
fileName = os.path.splitext(os.path.basename(__file__))[0]


import logging
log = logging.getLogger("Jewlery Tool")
#logFile = logging.getLogger("Jewlery Tool File")


#handlerStream = logging.StreamHandler()
handlerFile = logging.FileHandler('file.log')


# Create formatters and add it to handlers
#handlerStream.setFormatter(' ')
handlerFile.setFormatter(logging.Formatter('%(asctime)s|%(name)s|%(levelname)s|%(message)s'))
#handlerStream.setFormatter(streamFormat)
#handlerFile.setFormatter(fileFormat)

# Add handlers to the logger
log.addHandler(handlerFile)
#logFile.addHandler(handlerStream)

log.setLevel(logging.INFO)
#logFile.setLevel(logging.INFO)

#log.setLevel(logging.DEBUG)

log.info('{} loading'.format(fileName))


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





import string
log.debug('Imported String into {}'.format(fileName))

import pymel.core as pm
log.debug('Imported pymel.core into {}'.format(fileName))

import sys

from newTypeWindow import newTypeWindow
log.debug('Imported newTypeWindow into {}'.format(fileName))

from controlsDock import createControls
log.debug('Imported createControls into {}'.format(fileName))



log.info("Imported libraries into {}".format(fileName))



class MainWindow(QMainWindow):
    
    def new_pressed(self):
            log.info('New jewlery type button pressed')
            self.newTypeWin = newTypeWindow(self, self.ui.nameList)
            self.newTypeWin.show()
            log.debug('New jewlery type window opened')
    
    def __init__(self):
        log.debug('initializuing main window')
        if sys.version_info.major == 3:
            super().__init__()
        # python 2
        else:
            super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        
        self.ui.setupUi(self)

        
        #houdiniNodes = getAllObjects()
        self.ui.reloadAssetList()

        
            

        self.ui.new_bttn.clicked.connect(lambda: self.new_pressed())

        self.setWindowTitle("Jewlery Tool")

        log.info('main window initialized')

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        log.debug('Setting up main window ui')
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(877, 732)
        self.MainWindow = MainWindow
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(200, 0))
        self.groupBox.setMaximumSize(QSize(200, 123456))
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.new_bttn = QPushButton(self.groupBox)
        self.new_bttn.setObjectName(u"new_bttn")

        self.verticalLayout.addWidget(self.new_bttn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.groupBox)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setLayoutDirection(Qt.RightToLeft)
        self.label.setStyleSheet(u"background-color : grey")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.scrollArea = QScrollArea(self.groupBox_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 618, 624))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.inSceneViewer = QListWidget(self.scrollAreaWidgetContents)
        
        self.inSceneViewer.setObjectName(u"inSceneViewer")

        self.gridLayout.addWidget(self.inSceneViewer, 3, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.horizontalLayout_2.addWidget(self.groupBox_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.reloadButton = QPushButton("Reload")
        self.verticalLayout_2.addWidget(self.reloadButton)

        log.debug('Setting up signals and slots')
        self.reloadButton.clicked.connect(lambda: self.reloadAssetList())
        self.inSceneViewer.itemDoubleClicked.connect(lambda : self.toolDoubleClicked())#(n))
        log.debug('signals and slots set up')

        self.retranslateUi(MainWindow)

        log.debug('MainWindow UI created')

        

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def toolDoubleClicked(self):
        log.info('Item Double clicked on MainWindow List view')
        self.MainWindow.showMinimized()
        log.debug('main window minimized')
        doubleClickedItem = self.inSceneViewer.currentItem()
        if doubleClickedItem is not None:
            name = doubleClickedItem.text()

        name = name.split(" ")
        name = name[0]
        log.info('Item double clicked called {}'.format(name))
        log.debug('Creating reloaded controls')
        self.controls = createControls(self.MainWindow, name, 1)

    def reloadAssetList(self):
        log.info('reloading main window list view to contain all Jewlery types in scene')
        getTools = getAllObjects()
        self.nameList = []
        self.inSceneViewer.clear()
        log.debug('List of Jhumka Tools:')
        if(len(getTools.JhumkaToolList) == 0):
            log.debug("no jhumka tools in scene")
        for each in getTools.JhumkaToolList:
            name = str(each)
            name = name.split("_")
            name = name[0]
            log.debug('- {}'.format(name))
            self.nameList.append(name)
            stri = name + " Jhumka"
            #stri = stri.translate(string.maketrans('', ''), 'Node')
            self.inSceneViewer.addItem(stri)
        log.info('MainWindow List Reloaded')

    def retranslateUi(self, MainWindow):
        MainWindow.setProperty("Main Window", QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle("")
        self.new_bttn.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.groupBox_2.setTitle("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"In Scene", None))
    # retranslateUi

class getAllObjects():
    
    def __init__(self):
        log.debug('Getting all the pieces of jewlery in the scene')
        self.JhumkaToolList = []
        allObjects = pm.ls(l=True)
        
        #Creates an empty list called control_list that we'll use later
        self.control_list = []
        
        #Createss a for loop that goes through the list allObjects

        log.debug('List of all jewlery in the scene:')
        for obj in allObjects:
            
            if(type(obj) == pm.nodetypes.AttributeNode):
                self.JhumkaToolList.append(obj)
                log.debug('-{}'.format(obj))
                
class treeView(QTreeWidget):
    def __init__(self):
        if sys.version_info.major == 3:
            super().__init__()
        # python 2
        else:
            super(treeView, self).__init__()

