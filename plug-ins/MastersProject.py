from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import maya.api.OpenMaya as om
import maya.cmds as cmds
import sys 
import pymel.core as pm
import os

if not(cmds.pluginInfo( "attributeNode", query=True, loaded=True)):
    try:
       cmds.loadPlugin("attributeNode")
    except:
        om.MGlobal.displayError('Unable to load attribute node')

if not(cmds.pluginInfo( "houdiniEngine", query=True, loaded=True)):
    try:
        cmds.loadPlugin("houdiniEngine")

    except:
        om.MGlobal.displayError('Unable to load Houdini Enginge, please make sure this is installed')

plugin_root = os.environ.get("JEWLERYTOOLPLUGIN_ROOT")

pythonFilesPath = plugin_root + "/python-files/"

imageFilesPath = plugin_root + "/image-files/"

sys.path.append(pythonFilesPath)


from MainWindow import MainWindow

def maya_useNewAPI():

    pass


maya_useNewAPI = True

class JewleryTool(om.MPxCommand):

    CMD_NAME = "JewleryTool"

    def __init__(self):
        
        if sys.version_info.major == 3:
            super().__init__()
        # python 2
        else:
            super(JewleryTool, self).__init__()
        

    def doIt(self, args):

        if not QApplication.instance():
            app = QApplication(sys.argv)
        else:
            app = QApplication.instance()

        
        window = MainWindow()
        window.show()

        sys.exit(app.exec_())

    @classmethod
    def creator(cls):
        return JewleryTool()


class shelf():

    def doublun(self):
        if not(cmds.pluginInfo( "MastersProject", query=True, loaded=True)):
            cmds.loadPlugin("MastersProject")   
        cmds.JewleryTool()

    def __init__(self):
        
        if cmds.shelfLayout("JewlleryShelf", exists=1):
            pm.deleteUI("JewlleryShelf")
            
        
        cmds.shelfLayout("JewlleryShelf", parent="ShelfLayout")
            
        cmds.setParent("JewlleryShelf")
        cmds.shelfButton(width=100, height=100, image=(imageFilesPath+"jhumkaIcon.png"), l="JewlleryTool", olb=(0,0,0,0), olc=(0.9,0.9,0.9), command = self.doublun, imageOverlayLabel="Jewllery Tool")

        

            
            


def initializePlugin(plugin):
    vendor = "Matthew Stanton"
    version = "1.0.0"

    plugin_fn = om.MFnPlugin(plugin, vendor, version)

    shelf()

    try:
        plugin_fn.registerCommand(JewleryTool.CMD_NAME, JewleryTool.creator)
    except:
        om.MGlobal.displayError(
            "Failed to register command: {0}".format(JewleryTool.CMD_NAME)
        )


def uninitializePlugin(plugin):

    plugin_fn = om.MFnPlugin(plugin)
    pm.deleteUI("JewlleryShelf")
    try:
        plugin_fn.deregisterCommand(JewleryTool.CMD_NAME)
    except:
        om.MGlobal.displayError(
            "Failed to deregister command: {0}".format(JewleryTool.CMD_NAME)
        )


if __name__ == "__main__":

    plugin_name = "JewlleryTool.py"

    cmds.evalDeferred(
        'if cmds.pluginInfo("{0}", q=True, loaded=True): cmds.unloadPlugin("{0}")'.format(
            plugin_name
        )
    )
    cmds.evalDeferred(
        'if not cmds.pluginInfo("{0}", q=True, loaded=True): cmds.loadPlugin("{0}")'.format(
            plugin_name
        )
    )


