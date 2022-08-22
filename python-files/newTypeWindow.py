import os
fileName = os.path.splitext(os.path.basename(__file__))[0]

import logging




#logging.basicConfig()
log = logging.getLogger("Jewlery Tool")

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


import maya.api.OpenMaya as om
log.debug('imported OpenMayaAPI into {}'.format(fileName))

import sys

from nameJewleryPopup import nameJewleryPopup
log.debug('Imported nameJewleryPopup into {}'.format(fileName))

from controlsDock import createControls
log.debug('Imported createControls into {}'.format(fileName))

log.info("Imported libraries into {}".format(fileName))

plugin_root = os.environ.get("JEWLERYTOOLPLUGIN_ROOT")

imageFilesPath = plugin_root + "/image-files/"


class newTypeWindow(QMainWindow):
    def __init__(self, main_window, nameList):
        log.debug('Initializing {} QWidget'.format(fileName))
        
        self.main_window = main_window
        if sys.version_info.major == 3:
            super().__init__()
        # python 2
        else:
            super(newTypeWindow, self).__init__()

        
        self.ui = Ui_NewTypeWindow()
        self.ui.setupUi(self)
        image = imageFilesPath+"jhumkaIcon.png"

        img=QPixmap(image)
        icon=QIcon(img)
        self.ui.newJhumkaToolBtn.setIcon(icon)
        self.ui.newJhumkaToolBtn.setIconSize(QSize(100,100))
        log.debug('set image for Jhumka Type button')
        self.ui.newJhumkaToolBtn.clicked.connect(lambda checked: self.buttonPressed(checked))

        self.ui.createBtn.clicked.connect(lambda : self.createFunc(nameList))
        self.ui.createBtn.setEnabled(False)
        self.setWindowTitle("Select Type")
        log.info('{} widget initialized'.format(fileName))


    def createFunc(self, nameList):
        log.info('create button pushed')

        log.info('running name popup')
        namePopup = nameJewleryPopup(nameList)
        result = namePopup.exec_()
        log.info('name popup executed and returned {}'.format(result))

        #self.close()

        if(result):

            log.debug('running name error check on name {}'.format(namePopup.name))
            if( namePopup.Error == None):
                log.debug('no error returned')
                log.info("no error, popup returned name: %s"%namePopup.name)
                self.main_window.showMinimized()
                log.debug('creating new controls')
                self.controls = createControls(self.main_window, namePopup.name)
                log.debug('controls created')
                self.close()
                log.debug('NewTypeWindow closed')
                self.main_window.ui.reloadAssetList()

            elif(namePopup.Error == 1):
                log.error('error 1 returned: name contains only spaces')
                om.MGlobal.displayError("Jewlery Name Cannot Contain Only Spaces")

            elif(namePopup.Error == 2):
                log.error('error 2 returned: name is blank')
                om.MGlobal.displayError("Jewlery Name Cannot Be Left Blank")
                
            elif(namePopup.Error == 3):
                log.error('error 3 returned: name same as previous jewlery name')
                om.MGlobal.displayError("Jewlery Name Is the Same as Previous Jewlery Name")

            elif(namePopup.Error == 4):
                log.error('error 4 returned: name contains a space')
                om.MGlobal.displayError("Jewlery Name cannot contain spaces")

            

        else:
            log.info('name popup canceled')
            print("Rejected")

    def buttonPressed(self, checked):
        
        if(checked==1):
            log.info('Jhumka Tool checked')
            self.ui.createBtn.setEnabled(True)
        elif(checked==0):
            log.info('Jhumka Tool unchecked')
            self.ui.createBtn.setEnabled(False)






class Ui_NewTypeWindow(object):
    
    def setupUi(self, MainWindow):
        log.debug('setting up NewTypeWindow UI')
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(877, 732)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.createBtn = QPushButton(self.groupBox_2)
        self.createBtn.setObjectName(u"createBtn")
        self.createBtn.setMinimumSize(QSize(200, 0))

        self.gridLayout_3.addWidget(self.createBtn, 4, 1, 1, 1)

        self.groupBox = QGroupBox(self.groupBox_2)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.newJhumkaToolBtn = QToolButton(self.groupBox)
        self.newJhumkaToolBtn.setObjectName(u"newJhumkaToolBtn")
        self.newJhumkaToolBtn.setMinimumSize(QSize(100, 100))
        self.newJhumkaToolBtn.setAutoFillBackground(False)
        self.newJhumkaToolBtn.setCheckable(True)

        self.gridLayout.addWidget(self.newJhumkaToolBtn, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 1, 0, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 4, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setMaximumSize(QSize(16777215, 50))
        self.label.setLayoutDirection(Qt.RightToLeft)
        self.label.setStyleSheet(u"background-color : grey")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        log.debug('NewTypeWindow UI set up')
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setProperty("Main Window", QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_2.setTitle("")
        self.createBtn.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.groupBox.setTitle("")
        self.newJhumkaToolBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Jhumka", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"New Type", None))
    # retranslateUi

