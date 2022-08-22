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

log.info("Imported libraries into {}".format(fileName))


class nameJewleryPopup(QDialog):
    def __init__(self, nameList):

        log.info('initializing {} QDialog'.format(fileName))        
        
        super(nameJewleryPopup, self).__init__()
        self.ui = Ui_NameJewleryPopup()
        self.ui.setupUi(self, nameList)
        






class Ui_NameJewleryPopup(object):
    def setupUi(self, Dialog, nameList):
        log.debug('setting up {} UI'.format(fileName))
        self.nameList = nameList

        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 148)
    
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 1, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(lambda: self.accepted(Dialog))
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        

        QMetaObject.connectSlotsByName(Dialog)
        log.debug('set up {} UI'.format(fileName))

    # setupUi

    def accepted(self, Dialog):
        log.info('accept button clicked for {}'.format(fileName))
        Dialog.Error = None
        Dialog.name =  self.lineEdit.text()

        log.debug('checking jewlery name for error')
        if(Dialog.name.isspace()):
            log.debug('error 1 jewlery name is just spaces')
            Dialog.Error = 1

        elif(len(Dialog.name) == 0):
            log.debug('error 2 jewlery name is empty')
            Dialog.Error = 2

        elif(Dialog.name in self.nameList):
            log.debug('error 3 jewlery name is same as previous jewlery name')
            Dialog.Error = 3
        elif(' ' in Dialog.name):
            log.debug('error 4 space in jewlery name')
            Dialog.Error = 4
        else:
            log.debug('no error with jewlery name')


        
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Enter Jewlery Name:", None))
    # retranslateUi


    
    