import logging
#logging.basicConfig()
log = logging.getLogger("Jewlery Tool")

log.debug('nameJewleryPopup loading')
try:
    log.debug('trying to import PySide 2')
    from PySide2.QtCore import *
    from PySide2.QtGui import *
    from PySide2.QtWidgets import *
    # So we import wrapInstance from sip and alias it to wrapInstance so that it's the same as the others
    from shiboken2 import wrapInstance
    log.debug('Using PySide2 and Shiboken2')


except:
    log.debug('PySide 2 not avalable')
    try:
        log.debug('trying to import PySide')
        from PySide.QtCore import *
        from PySide.QtGui import *
        from PySide.QtWidgets import *
        # So we import wrapInstance from sip and alias it to wrapInstance so that it's the same as the others
        from shiboken import wrapinstance 
        log.debug('Using PySide and Shiboken')


    except:
        log.debug('Pyside not avalable')
        try:
            log.debug('trying to import PyQt5')
            from PyQt5.QtCore import *
            from PyQt5.QtGui import *
            from PyQt5.QtWidgets import *
            # So we import wrapInstance from sip and alias it to wrapInstance so that it's the same as the others
            from sip import wrapinstance as wrapInstance
            log.debug('Using PyQt5 and sip')

        except:
            log.debug('PyQt5 not avalable')
            log.debug('trying to import PyQt4')
            from PyQt4.QtCore import *
            from PyQt4.QtGui import *
            from PyQt4.QtWidgets import *
            # So we import wrapInstance from sip and alias it to wrapInstance so that it's the same as the others
            from sip import wrapinstance as wrapInstance
            log.debug('Using PyQt4 and sip')

import os

plugin_root = os.environ.get("JEWLERYTOOLPLUGIN_ROOT")

imageFilesPath = plugin_root + "/image-files/"

import pymel.core as pm
log.debug('pymel.core imported')

import maya.cmds as cmds
log.debug('maya.cmds imported')

import maya.api.OpenMaya as om
log.debug('OpenMaya imported')

import sys

from createVariableSlider import createVariableSlider
log.debug('createVariableSlider imported')

class createMainJhumkaTabWidget(QWidget):
    def __init__(self, name):
        if sys.version_info.major == 3:
            super().__init__()
        # python 2
        else:
            super(createMainJhumkaTabWidget, self).__init__()
        self.name = name
        self.setupUi()

    def setupUi(self):
        log.info('creating tab UI for {}'.format(self.name))
        # self.layout = QGridLayout(self)
        # self.scrollArea = QScrollArea(self)
        # self.scrollArea.setObjectName(self.name+"_scrollArea")
        # self.scrollArea.setWidgetResizable(True)
        # self.scrollAreaWidgetContents = QWidget()
        # self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        # self.scrollAreaWidgetContents.setGeometry(QRect(0, -146, 245, 253))
        self.scrollLayout = QGridLayout(self)
        self.scrollLayout.setObjectName(u"gridLayout_4")
        # self.layout.addWidget(self.scrollArea, 0, 0, 1, 1)
        # self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        # self.scrollArea.setFrameShape(QFrame.NoFrame)
        # self.scrollLayout.setContentsMargins(0, 0 ,0 , 0)
        # self.scrollArea.setContentsMargins(0, 0 ,0 , 0)


        
        #self.layout = QGridLayout(self)
        self.checkBox = QCheckBox("Remove Rings")
        
        self.checkBox.setObjectName(self.name+"_checkBox")

        self.scrollLayout.addWidget(self.checkBox, 0, 0, 1, 1)
        
        self.ringRadius = createVariableSlider("Rings Radius", 0.01, 0.2, 0 ,single_step=0.01)
        self.scrollLayout.addWidget(self.ringRadius, 1, 0, 1, 3)
        

        self.label = QLabel("Detail Type")
        self.scrollLayout.addWidget(self.label,  2, 0, 1, 1)
        
        comboList = ["Sphere", "Line", "File"]
        self.comboBox = QComboBox()
        self.comboBox.setObjectName(self.name+"_comboBox")
        self.comboBox.addItems(comboList)
        self.comboBox.currentIndexChanged.connect(lambda n: self.indexChanged(n))

        self.scrollLayout.addWidget(self.comboBox, 2, 1, 1, 1)

        self.repeatedDetailSlider = createVariableSlider("Repeat Amount", 30, 100, 1 ,single_step=1)
        self.scrollLayout.addWidget(self.repeatedDetailSlider, 3, 0, 1, 3)

        self.scaleSlider = createVariableSlider("Scale", 1, 5, 0 ,single_step=0.05)
        self.scrollLayout.addWidget(self.scaleSlider, 4, 0, 1, 3)

        
        

        self.heightSlider = createVariableSlider("Height", 1, 5, 0 ,single_step=0.05)
        self.scrollLayout.addWidget(self.heightSlider, 5, 0, 1, 3)

        self.depthSlider = createVariableSlider("Depth", 1, 5, 0 ,single_step=0.05)
        self.scrollLayout.addWidget(self.depthSlider, 6, 0, 1, 3)

        self.rotationSlider = createVariableSlider("Rotation", 0, 360, 0 ,single_step=15)
        self.scrollLayout.addWidget(self.rotationSlider, 7 , 0, 1, 3)

        self.fileSelector = fileSelector("File")
        self.scrollLayout.addWidget(self.fileSelector, 8 , 0, 1, 3)
        self.fileSelector.setEnabled(False)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.verticalSpacer = QSpacerItem(20, 28, QSizePolicy.Maximum, QSizePolicy.Expanding)

        self.scrollLayout.addItem(self.verticalSpacer, 10, 1, 1, 1)

        #self.setMaximumHeight(100)

    def indexChanged(self, n):
        log.debug('combobox changed in {} {} tab to index {}'.format(self.name, self, n))
        if( n == 2 ):
            self.fileSelector.setEnabled(True)
            log.debug('file selector enabled')
            
        else:
            self.fileSelector.setEnabled(False)
            log.debug('file selector disabled')

class fileSelector(QWidget):

    def __init__(self, name):
        log.debug('file selector widget initializing for {} controls'.format(name))
        self.name = name
        self.window_name = 'Test'

        if sys.version_info.major == 3:
            super().__init__()
        # python 2
        else:
            super(fileSelector, self).__init__()
        
        
        
        
        self.setupUi()
        log.debug('file selector widget initialized')

    def setupUi(self):
        log.debug('setting up file selector UI in {} controls'.format(self.name))
        layout = QHBoxLayout(self)
        layout.setSpacing(0)
        self.label = QLabel("Pattern File")
        self.label.setObjectName(self.name+"_label")

        layout.addWidget(self.label)

        
        self.fileNameLineEdit = QLineEdit("Pattern File")
        self.fileNameLineEdit.setText("{}pattern.png".format(imageFilesPath))

        layout.addWidget(self.fileNameLineEdit)

        
        self.selectFileButton = QPushButton()
        icon = QIcon(":/fileOpen.png")
        self.selectFileButton.setIcon(icon)
        self.selectFileButton.setFixedSize(18,18)
        self.selectFileButton.setIconSize(QSize(15,15))
        #icon = QIcon(QIcon.fromTheme(u"edit-copy"))
        self.selectFileButton.clicked.connect(lambda: self.selectFileButtonPushed())

        #self.selectFileButton.setIcon(icon)
        layout.addWidget(self.selectFileButton)

    def selectFileButtonPushed(self):
        log.debug('file selector choose file button pushed in {} controls'.format(self.name))
        name,_ = QFileDialog.getOpenFileName(self, directory = "~/", filter = ( "PNG (*.png);; JPEG(*.jpg, *.jpeg);; TIFF(.*tif, *.tif3, *.tif16, *.tif32, *.tiff);; PIC(*.pic, *.pic.Z, *.picZ, *.pic.gz, *.picgz, *.picnc, *.piclc, *.rat);; TBF(*.tbf);; DSM(*.dsm);; RGB BITMAP(*.rgb, *.rgba);; SGI(.*sgi, .*rla, *.rla16);;  YUV(*.yuv);; PIX(*.pix);; ALS(*.als);; CIN(*.cin);; KDK(*.kdk);; Photoshop(*.psd);; Large Document(*.psb);; SI(*.si);; TARGA(*.tga);; VST(*.vst);; VTG(*.vtg);;  RLB(*.rlb);; BMP(*.bmp);; Radiance(*.hdr);; PTX(*.ptx);; PTEX(*.ptex);; Photometric Pass(*.ies);; Direct Draw(*dds);; R(*.r16, *.r32);; QTL(*.gtl);; Any Files(*)"))
        name = str(name)
        log.debug('file {} chosen using file Dialog'.format(name))
        try:
            #Gets the text from within the file selected by the user and reads each line into a list
            with open(name, 'r') as f:
                print(name)
                self.fileNameLineEdit.setText(name)
                log.debug('set file line edit to {}'.format(name))
                #self.glslCodeEditor.setText(text)
                f.close()

        except:
            log.debug('error {} texture file cannot be opened'.format(name))
            om.MGlobal.displayError("Cannot Open Texture File")