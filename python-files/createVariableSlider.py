import logging
import os
#logging.basicConfig()
fileName = os.path.splitext(os.path.basename(__file__))[0]
log = logging.getLogger("Jewlery Tool")

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
log.debug('imported pymel.core')
import maya.cmds as cmds 
log.debug('imported maya.cmds')

import sys

log.debug('loading createVariableSlider')

class createVariableSlider(QWidget):
    def __init__(self, name, value=50, max=100, int=1, parent = None, single_step = 0.05):

        log.debug('initializing createVariableSlider QWidget for {}'.format(name))
        

        self.name = name
        self.int = int
        
        
        self.value_spinBox = value
        self.max_spinBox = max
        self.single_step_spinBox = single_step
        log.debug('setting max values')
        if(self.int):
            self.value_slider = value
            self.max_slider = max
            self.single_step = single_step
            log.debug('max value set as int')
        else:
            self.value_slider = value * 1000
            self.max_slider = max * 1000
            self.single_step = single_step * 1000
            log.debug('max value set as float')
        
        


        
        self.window_name = 'Test'

        if sys.version_info.major == 3:
            super().__init__()
        # python 2
        else:
            super(createVariableSlider, self).__init__()
        
        
        
        
        self.setupUi()

        log.debug('variable slider initialized with variables: | name = {} | value = {} | max = {} | isInt = {} | parent = {} |'.format(name, value, max, int, parent))

    def setupUi(self):
        log.debug('setting up variable slider UI')
        layout = QHBoxLayout(self)
        self.label = QLabel(self.name)
        self.label.setObjectName(self.name+"_label")

        layout.addWidget(self.label)

        if(self.int):
            self.spinBox = QSpinBox()
        else:
            self.spinBox = QDoubleSpinBox()

        self.spinBox.setObjectName(self.name+"_spinBox")
        self.spinBox.setValue(self.value_spinBox)
        self.spinBox.setMaximum(self.max_spinBox)
        self.spinBox.setSingleStep(self.single_step_spinBox)

        layout.addWidget(self.spinBox)

        self.slider = QSlider()
        self.slider.setObjectName(self.name+"_slider")
        self.slider.setMaximum(self.max_slider)
        self.slider.setValue(self.value_slider)
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setSingleStep(self.single_step)

        layout.addWidget(self.slider)
        if(self.int):
            self.intSetupSignalsSlots()
        else:
            self.floatSetupSignalsSlots()

    def intSetupSignalsSlots(self):
        log.debug('setting up int signals and slots for {}'.format(self.name))
        self.slider.valueChanged.connect(lambda val : self.intSliderChanged(val))
        self.spinBox.valueChanged.connect(lambda val : self.intSpinBoxChanged(val))

    def floatSetupSignalsSlots(self):
        log.debug('setting up float signals and slots for {}'.format(self.name))
        self.slider.valueChanged.connect(lambda val : self.floatSliderChanged(val))
        self.spinBox.valueChanged.connect(lambda val : self.floatSpinBoxChanged(val))

    def intSliderChanged(self, n):
        self.spinBox.setValue(n)
        

    def floatSliderChanged(self, n):
        n = float(n)    
        n = n/1000
        self.spinBox.setValue(n)
        

    def intSpinBoxChanged(self, n):

        self.slider.setValue(n)
        log.info('{} value changed to {}'.format(self.name, n))

    def floatSpinBoxChanged(self, n):
        n = n * 1000
        n = int(n)
        self.slider.setValue(n)
        log.info('{} value changed to {}'.format(self.name, n))
