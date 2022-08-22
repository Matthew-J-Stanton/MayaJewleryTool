from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import maya.api.OpenMaya as om
import maya.cmds as cmds
import sys 
import maya.cmds as cmds
import os

if not(cmds.pluginInfo( "attributeNode", query=True, loaded=True)):
    cmds.loadPlugin("attributeNode")

if not(cmds.pluginInfo( "houdiniEngine", query=True, loaded=True)):
    cmds.loadPlugin("houdiniEngine")

plugin_root = os.environ.get("JEWLERYTOOLPLUGIN_ROOT")

#mainWindowfile = plugin_root + "/python-files/MainWindow.py"
#sys.path.append(mainWindowfile)

from MainWindow import MainWindow

def maya_useNewAPI():
    """
    Can either use this function (which works on earlier versions)
    or we can set maya_useNewAPI = True
    """
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
        """
        Called when the command is executed in script
        """
        if not QApplication.instance():
            app = QApplication(sys.argv)
        else:
            app = QApplication.instance()

        
        window = MainWindow()
        window.show()

        sys.exit(app.exec_())

    @classmethod
    def creator(cls):
        """
        Think of this as a factory
        """
        return JewleryTool()


def initializePlugin(plugin):
    """
    Load our plugin
    """
    vendor = "NCCA"
    version = "1.0.0"

    plugin_fn = om.MFnPlugin(plugin, vendor, version)

    try:
        plugin_fn.registerCommand(JewleryTool.CMD_NAME, JewleryTool.creator)
    except:
        om.MGlobal.displayError(
            "Failed to register command: {0}".format(JewleryTool.CMD_NAME)
        )


def uninitializePlugin(plugin):
    """
    Exit point for a plugin
    """
    plugin_fn = om.MFnPlugin(plugin)
    try:
        plugin_fn.deregisterCommand(JewleryTool.CMD_NAME)
    except:
        om.MGlobal.displayError(
            "Failed to deregister command: {0}".format(JewleryTool.CMD_NAME)
        )


if __name__ == "__main__":
    """
    So if we execute this in the script editor it will be a __main__ so we can put testing code etc here
    Loading the plugin will not run this
    As we are loading the plugin it needs to be in the plugin path.
    """

    plugin_name = "JewleryTool.py"

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


