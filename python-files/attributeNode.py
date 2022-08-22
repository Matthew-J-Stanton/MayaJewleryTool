
import maya.api.OpenMaya as om
import maya.OpenMayaMPx as ompx
import maya.cmds as cmds
import sys

maya_useNewAPI = True

#class AttributeNodeCommand(om.MPxCommand):

class AttributeNode(om.MPxNode):

    inMainTabsScale = []
    outMainTabsScale = []
    
    
    nodeName = "AttributeNode"
    nodeId = om.MTypeId(0x70000)

    inRows = om.MObject()
    inColumns = om.MObject()
    inScale = om.MObject()
    inStretch = om.MObject()
    inJhumkaAmount = om.MObject()
    inDangleSize = om.MObject()
    inJewelSize = om.MObject()
    inNumOfSec = om.MObject()
    inRingRadius = om.MObject()
    inHookCircleRad = om.MObject()
    inBlendJhumka = om.MObject()

    inMainRemoveRing = om.MObject()
    inMainRingRadius = om.MObject()
    inMainDetailType = om.MObject()
    inMainRepeatAmount = om.MObject()
    inMainTabScale = om.MObject()
    inMainHeight = om.MObject()
    inMainDepth = om.MObject()
    inMainRotation = om.MObject()
    inMainFilePath = om.MObject()

    inHookRemoveRing = om.MObject()
    inHookRingRadius = om.MObject()
    inHookDetailType = om.MObject()
    inHookRepeatAmount = om.MObject()
    inHookTabScale = om.MObject()
    inHookHeight = om.MObject()
    inHookDepth = om.MObject()
    inHookRotation = om.MObject()
    inHookFilePath = om.MObject()

    outRows = om.MObject()
    outColumns = om.MObject()
    outScale = om.MObject()
    outStretch = om.MObject()
    outJhumkaAmount = om.MObject()
    outDangleSize = om.MObject()
    outJewelSize = om.MObject()
    outNumOfSec = om.MObject()
    outRingRadius = om.MObject()
    outHookCircleRad = om.MObject()
    outBlendJhumka = om.MObject()

    def __init__(self):
        om.MPxNode.__init__(self)
       

    def compute(self, plug, dataBlock):

        if(plug == self.outRows or plug == self.outColumns or plug == self.outScale or plug == self.outStretch  or plug == self.outJewelSize or plug == self.outNumOfSec or plug == self.outRingRadius or plug == self.outHookCircleRad or plug == self.outDangleSize ):
            dataHandleRows = dataBlock.inputValue(AttributeNode.inRows) 
            inRowsVal = dataHandleRows.asFloat()

            dataHandleColumns = dataBlock.inputValue(AttributeNode.inColumns) 
            inColumnsVal = dataHandleColumns.asFloat()

            dataHandleScale = dataBlock.inputValue(AttributeNode.inScale) 
            inScaleVal = dataHandleScale.asFloat()

            dataHandleStretch = dataBlock.inputValue(AttributeNode.inStretch)
            inStretchVal = dataHandleStretch.asFloat()

            

            dataHandleDangleSize = dataBlock.inputValue(AttributeNode.inDangleSize)
            inDangleSizeVal = dataHandleDangleSize.asFloat()

            dataHandleJewelSize = dataBlock.inputValue(AttributeNode.inJewelSize)
            inJewelSizeVal = dataHandleJewelSize.asFloat()

            dataHandleNumOfSec = dataBlock.inputValue(AttributeNode.inNumOfSec)
            inNumOfSecVal = dataHandleNumOfSec.asFloat()

            dataHandleRingRadius = dataBlock.inputValue(AttributeNode.inRingRadius)
            inRingRadiusVal = dataHandleRingRadius.asFloat()

            dataHandleHookCircleRad = dataBlock.inputValue(AttributeNode.inHookCircleRad)
            inHookCircleVal = dataHandleHookCircleRad.asFloat()

            

            

            outRows = inRowsVal
            dataHandleOutRows = dataBlock.outputValue(AttributeNode.outRows)
            dataHandleOutRows.setFloat(outRows)
            dataBlock.setClean(plug)

            outColumns = inColumnsVal
            dataHandleOutColumns = dataBlock.outputValue(AttributeNode.outColumns)
            dataHandleOutColumns.setFloat(outColumns)
            dataBlock.setClean(plug)

            outScale = inScaleVal
            dataHandleOutScale = dataBlock.outputValue(AttributeNode.outScale)
            dataHandleOutScale.setFloat(outScale)
            dataBlock.setClean(plug)

            outStretch = inStretchVal
            dataHandleOutStretch = dataBlock.outputValue(AttributeNode.outStretch)
            dataHandleOutStretch.setFloat(outStretch)
            dataBlock.setClean(plug)

            

            outDangleSize = inDangleSizeVal
            dataHandleOutDangleSize = dataBlock.outputValue(AttributeNode.outDangleSize)
            dataHandleOutDangleSize.setFloat(outDangleSize)
            dataBlock.setClean(plug)

            outJewelSize = inJewelSizeVal
            dataHandleOutJewelSize = dataBlock.outputValue(AttributeNode.outJewelSize)
            dataHandleOutJewelSize.setFloat(outJewelSize)
            dataBlock.setClean(plug)

            outNumOfSec = inNumOfSecVal
            dataHandleOutNumOfSec = dataBlock.outputValue(AttributeNode.outNumOfSec)
            dataHandleOutNumOfSec.setFloat(outNumOfSec)
            dataBlock.setClean(plug)

            outRingRadius = inRingRadiusVal
            dataHandleOutRingRadius = dataBlock.outputValue(AttributeNode.outRingRadius)
            dataHandleOutRingRadius.setFloat(outRingRadius)
            dataBlock.setClean(plug)

            outHookCircleRad = inHookCircleVal
            dataHandleOutHookCircleRad = dataBlock.outputValue(AttributeNode.outHookCircleRad)
            dataHandleOutHookCircleRad.setFloat(outHookCircleRad)
            dataBlock.setClean(plug)

            
            

        elif(plug == self.outJhumkaAmount):
            dataHandleJhumkaAmount = dataBlock.inputValue(AttributeNode.inJhumkaAmount)
            inJhumkaAmountVal = dataHandleJhumkaAmount.asFloat()

            outJhumkaAmount = inJhumkaAmountVal
            dataHandleOutJhumkaAmount = dataBlock.outputValue(AttributeNode.outJhumkaAmount)
            dataHandleOutJhumkaAmount.setFloat(outJhumkaAmount)
            dataBlock.setClean(plug)

        elif( plug == self.outBlendJhumka ):
            dataHandleBlendJhumka = dataBlock.inputValue(AttributeNode.inBlendJhumka)
            inBlendJhumkaa = dataHandleBlendJhumka.asFloat()

            outBlendJhumkaa = inBlendJhumkaa
            dataHandleOutBlendJhumka = dataBlock.outputValue(AttributeNode.outBlendJhumka)
            dataHandleOutBlendJhumka.setFloat(outBlendJhumkaa)
            dataBlock.setClean(plug)

        else:
            return


        


    
    @staticmethod
    def nodeInitializer():
        attr = om.MFnNumericAttribute()
        stringAttr= om.MFnTypedAttribute()

        AttributeNode.inRows = attr.create("rows", "r", om.MFnNumericData.kInt, 50)
        attr.readable = True
        attr.writable = True
        attr.keyable = True
        attr.storable = True
        # attr.setWritable(True)
        
        om.MPxNode.addAttribute(AttributeNode.inRows)

        AttributeNode.inColumns = attr.create("columns", "c", om.MFnNumericData.kInt, 27)
        attr.readable = True
        attr.writable = True
        attr.keyable = True
        attr.storable = True

        om.MPxNode.addAttribute(AttributeNode.inColumns)

        AttributeNode.inScale = attr.create("scale", "s", om.MFnNumericData.kFloat, 1.5)
        attr.readable = True
        attr.writable = True
        attr.keyable = True
        attr.storable = True

        om.MPxNode.addAttribute(AttributeNode.inScale)

        AttributeNode.inStretch = attr.create("stretch", "str", om.MFnNumericData.kFloat, 1.15)
        attr.readable = True
        attr.writable = True
        attr.keyable = True
        attr.storable = True

        om.MPxNode.addAttribute(AttributeNode.inStretch)

        AttributeNode.inJhumkaAmount = attr.create("jhumkaAmount", "ja", om.MFnNumericData.kInt, 10)
        attr.readable = True
        attr.writable = True
        attr.keyable = True
        attr.storable = True

        om.MPxNode.addAttribute(AttributeNode.inJhumkaAmount)

        AttributeNode.inDangleSize = attr.create("dangleSize", "ds", om.MFnNumericData.kFloat, 1)
        attr.readable = True
        attr.writable = True
        attr.keyable = True
        attr.storable = True

        om.MPxNode.addAttribute(AttributeNode.inDangleSize)

        AttributeNode.inJewelSize= attr.create("jewelSize", "js", om.MFnNumericData.kFloat, 1)
        attr.readable = True
        attr.writable = True
        attr.keyable = True
        attr.storable = True

        om.MPxNode.addAttribute(AttributeNode.inJewelSize)

        AttributeNode.inNumOfSec = attr.create("numOfSec", "nos", om.MFnNumericData.kInt, 6)
        attr.readable = True
        attr.writable = True
        attr.keyable = True
        attr.storable = True

        om.MPxNode.addAttribute(AttributeNode.inNumOfSec)

        AttributeNode.inRingRadius = attr.create("ringRadius", "rr", om.MFnNumericData.kFloat, 0.02)
        attr.readable = True
        attr.writable = True
        attr.keyable = True
        attr.storable = True

        om.MPxNode.addAttribute(AttributeNode.inRingRadius)

        AttributeNode.inHookCircleRad= attr.create("HookCircleRadius", "hcr", om.MFnNumericData.kFloat, 0.98)
        attr.readable = True
        attr.writable = True
        attr.keyable = True
        attr.storable = True

        om.MPxNode.addAttribute(AttributeNode.inHookCircleRad)

        AttributeNode.inBlendJhumka = attr.create("BlendJhumka", "bj", om.MFnNumericData.kFloat, 0)
        attr.readable = True
        attr.writable = True
        attr.keyable = True
        attr.storable = True

        om.MPxNode.addAttribute(AttributeNode.inBlendJhumka)






        outAttr = om.MFnNumericAttribute()
        AttributeNode.outRows = outAttr.create("outRows", "or", om.MFnNumericData.kInt)
        outAttr.readable = True
        outAttr.writable = False
        outAttr.keyable = False
        outAttr.storable = False

        om.MPxNode.addAttribute(AttributeNode.outRows)

        AttributeNode.outColumns = outAttr.create("outColumns", "oc", om.MFnNumericData.kInt)
        outAttr.readable = True
        outAttr.writable = False
        outAttr.keyable = False
        outAttr.storable = False

        om.MPxNode.addAttribute(AttributeNode.outColumns)

        AttributeNode.outScale = outAttr.create("outScale", "os", om.MFnNumericData.kFloat)
        outAttr.readable = True
        outAttr.writable = False
        outAttr.keyable = False
        outAttr.storable = False

        om.MPxNode.addAttribute(AttributeNode.outScale)

        AttributeNode.outStretch = outAttr.create("outStretch", "ost", om.MFnNumericData.kFloat)
        outAttr.readable = True
        outAttr.writable = False
        outAttr.keyable = False
        outAttr.storable = False

        om.MPxNode.addAttribute(AttributeNode.outStretch)

        AttributeNode.outJhumkaAmount = outAttr.create("outJhumkaAmount", "oja", om.MFnNumericData.kInt)
        outAttr.readable = True
        outAttr.writable = False
        outAttr.keyable = False
        outAttr.storable = False

        om.MPxNode.addAttribute(AttributeNode.outJhumkaAmount)

        AttributeNode.outDangleSize = outAttr.create("outDangleSize", "od", om.MFnNumericData.kFloat)
        outAttr.readable = True
        outAttr.writable = False
        outAttr.keyable = False
        outAttr.storable = False

        om.MPxNode.addAttribute(AttributeNode.outDangleSize)

        AttributeNode.outJewelSize = outAttr.create("outJewelSize", "oj", om.MFnNumericData.kFloat)
        outAttr.readable = True
        outAttr.writable = False
        outAttr.keyable = False
        outAttr.storable = False

        om.MPxNode.addAttribute(AttributeNode.outJewelSize)

        AttributeNode.outNumOfSec = outAttr.create("outNumOfSec", "onos", om.MFnNumericData.kInt)
        outAttr.readable = True
        outAttr.writable = False
        outAttr.keyable = False
        outAttr.storable = False

        om.MPxNode.addAttribute(AttributeNode.outNumOfSec)

        AttributeNode.outRingRadius = outAttr.create("outRingRadius", "orr", om.MFnNumericData.kFloat)
        outAttr.readable = True
        outAttr.writable = False
        outAttr.keyable = False
        outAttr.storable = False

        om.MPxNode.addAttribute(AttributeNode.outRingRadius)

        AttributeNode.outHookCircleRad = outAttr.create("outHookCircleRad", "ohcr", om.MFnNumericData.kFloat)
        outAttr.readable = True
        outAttr.writable = False
        outAttr.keyable = False
        outAttr.storable = False

        om.MPxNode.addAttribute(AttributeNode.outHookCircleRad)

        AttributeNode.outBlendJhumka = outAttr.create("outBlendJhumka", "obj", om.MFnNumericData.kFloat)
        outAttr.readable = True
        outAttr.writable = False
        outAttr.keyable = False
        outAttr.storable = False

        om.MPxNode.addAttribute(AttributeNode.outBlendJhumka)

        
        attr = om.MFnNumericAttribute()
 
   
   
        for each in range(0, 50):

            AttributeNode.inMainRemoveRing = attr.create("mainTabRemoveRing_{}".format(each), "mremover_{}".format(each), om.MFnNumericData.kBoolean, 0)
            attr.readable = True
            attr.writable = True
            attr.keyable = True
            attr.storable = True
            om.MPxNode.addAttribute(AttributeNode.inMainRemoveRing)
            
            AttributeNode.inMainRingRadius = attr.create("mainTabRingRadius_{}".format(each), "mrr_{}".format(each), om.MFnNumericData.kFloat, 0.01)
            attr.readable = True
            attr.writable = True
            attr.keyable = True
            attr.storable = True
            om.MPxNode.addAttribute(AttributeNode.inMainRingRadius)

            AttributeNode.inMainDetailType = attr.create("mainTabDetailType_{}".format(each), "mdt_{}".format(each), om.MFnNumericData.kInt, 0)
            attr.readable = True
            attr.writable = True
            attr.keyable = True
            attr.storable = True
            om.MPxNode.addAttribute(AttributeNode.inMainDetailType)

            AttributeNode.inMainRepeatAmount = attr.create("mainTabRepeatAmount_{}".format(each), "mtra_{}".format(each), om.MFnNumericData.kInt, 30)
            attr.readable = True
            attr.writable = True
            attr.keyable = True
            attr.storable = True
            om.MPxNode.addAttribute(AttributeNode.inMainRepeatAmount)
            
            AttributeNode.inMainTabScale = attr.create("mainTabScale_{}".format(each), "ms_{}".format(each), om.MFnNumericData.kFloat, 1)
            attr.readable = True
            attr.writable = True
            attr.keyable = True
            attr.storable = True
            om.MPxNode.addAttribute(AttributeNode.inMainTabScale)

            AttributeNode.inMainHeight = attr.create("mainTabHeight_{}".format(each), "mh_{}".format(each), om.MFnNumericData.kFloat, 1)
            attr.readable = True
            attr.writable = True
            attr.keyable = True
            attr.storable = True
            om.MPxNode.addAttribute(AttributeNode.inMainHeight)

            AttributeNode.inMainDepth = attr.create("mainTabDepth_{}".format(each), "md_{}".format(each), om.MFnNumericData.kFloat, 1)
            attr.readable = True
            attr.writable = True
            attr.keyable = True
            attr.storable = True
            om.MPxNode.addAttribute(AttributeNode.inMainDepth)

            AttributeNode.inMainRotation = attr.create("mainTabRotation_{}".format(each), "mr_{}".format(each), om.MFnNumericData.kFloat, 0)
            attr.readable = True
            attr.writable = True
            attr.keyable = True
            attr.storable = True
            om.MPxNode.addAttribute(AttributeNode.inMainRotation)

            # AttributeNode.inMainFilePath = strAttr.create("mainFilePath_{}".format(each), "mfp_{}".format(each), om.MFnData.kString, "tes") 
            # strAttr.readable = True
            # strAttr.writable = True
            # strAttr.keyable = True
            # strAttr.storable = True
            # om.MPxNode.addAttribute(AttributeNode.inMainFilePath)

            inputString = om.MFnStringData().create("<FilePathIn>")
            AttributeNode.inMainFilePath = stringAttr.create("mainFilePath_{}".format(each), "mfp_{}".format(each), om.MFnData.kString, inputString)
            # Attaching input Attributes
            AttributeNode.addAttribute(AttributeNode.inMainFilePath)

#####################################################################################################################################################################

            AttributeNode.inHookRemoveRing = attr.create("hookTabRemoveRing_{}".format(each), "hremover_{}".format(each), om.MFnNumericData.kBoolean, 0)
            attr.readable = True
            attr.writable = True
            attr.keyable = True
            attr.storable = True
            om.MPxNode.addAttribute(AttributeNode.inHookRemoveRing)

            AttributeNode.inHookRingRadius = attr.create("hookTabRingRadius_{}".format(each), "hrr_{}".format(each), om.MFnNumericData.kFloat, 0.01)
            attr.readable = True
            attr.writable = True
            attr.keyable = True
            attr.storable = True
            om.MPxNode.addAttribute(AttributeNode.inHookRingRadius)

            AttributeNode.inHookDetailType = attr.create("hookTabDetailType_{}".format(each), "hdt_{}".format(each), om.MFnNumericData.kInt, 0)
            attr.readable = True
            attr.writable = True
            attr.keyable = True
            attr.storable = True
            om.MPxNode.addAttribute(AttributeNode.inHookDetailType)

            AttributeNode.inHookRepeatAmount = attr.create("hookTabRepeatAmount_{}".format(each), "htra_{}".format(each), om.MFnNumericData.kInt, 30)
            attr.readable = True
            attr.writable = True
            attr.keyable = True
            attr.storable = True
            om.MPxNode.addAttribute(AttributeNode.inHookRepeatAmount)
            
            AttributeNode.inHookTabScale = attr.create("hookTabScale_{}".format(each), "hs_{}".format(each), om.MFnNumericData.kFloat, 1)
            attr.readable = True
            attr.writable = True
            attr.keyable = True
            attr.storable = True
            om.MPxNode.addAttribute(AttributeNode.inHookTabScale)

            AttributeNode.inHookHeight = attr.create("hookTabHeight_{}".format(each), "hh_{}".format(each), om.MFnNumericData.kFloat, 1)
            attr.readable = True
            attr.writable = True
            attr.keyable = True
            attr.storable = True
            om.MPxNode.addAttribute(AttributeNode.inHookHeight)

            AttributeNode.inHookDepth = attr.create("hookTabDepth_{}".format(each), "hd_{}".format(each), om.MFnNumericData.kFloat, 1)
            attr.readable = True
            attr.writable = True
            attr.keyable = True
            attr.storable = True
            om.MPxNode.addAttribute(AttributeNode.inHookDepth)

            AttributeNode.inHookRotation = attr.create("hookTabRotation_{}".format(each), "hr_{}".format(each), om.MFnNumericData.kFloat, 0)
            attr.readable = True
            attr.writable = True
            attr.keyable = True
            attr.storable = True
            om.MPxNode.addAttribute(AttributeNode.inHookRotation)

            inputString = om.MFnStringData().create("<FilePathIn>")
            AttributeNode.inHookFilePath = stringAttr.create("hookFilePath_{}".format(each), "hfp_{}".format(each), om.MFnData.kString, inputString)
            # Attaching input Attributes
            AttributeNode.addAttribute(AttributeNode.inHookFilePath)


        

        om.MPxNode.attributeAffects(AttributeNode.inRows, AttributeNode.outRows)
        om.MPxNode.attributeAffects(AttributeNode.inColumns, AttributeNode.outColumns)
        om.MPxNode.attributeAffects(AttributeNode.inScale, AttributeNode.outScale)
        om.MPxNode.attributeAffects(AttributeNode.inStretch, AttributeNode.outStretch)
        om.MPxNode.attributeAffects(AttributeNode.inJhumkaAmount, AttributeNode.outJhumkaAmount)
        om.MPxNode.attributeAffects(AttributeNode.inDangleSize, AttributeNode.outDangleSize)
        om.MPxNode.attributeAffects(AttributeNode.inJewelSize, AttributeNode.outJewelSize)
        om.MPxNode.attributeAffects(AttributeNode.inNumOfSec, AttributeNode.outNumOfSec)
        om.MPxNode.attributeAffects(AttributeNode.inRingRadius, AttributeNode.outRingRadius)
        om.MPxNode.attributeAffects(AttributeNode.inHookCircleRad, AttributeNode.outHookCircleRad)
        om.MPxNode.attributeAffects(AttributeNode.inBlendJhumka, AttributeNode.outBlendJhumka)


    @staticmethod
    def createNode():
        return AttributeNode() 
        #return ompx.asMPxPtr( AttributeNode() )

def initializePlugin(obj):
    """
    Load our plugin
    """
    vendor = "Matthew Stanton"
    version = "1.0.0"

    plugin = om.MFnPlugin(obj)

    try:
        plugin.registerNode("AttributeNode", AttributeNode.nodeId, AttributeNode.createNode, AttributeNode.nodeInitializer)
    except Exception as e:
        print("exception - {0}".format(e))
        om.MGlobal.displayError(
            "Failed to register command: {0}".format(AttributeNode.nodeName)
        )


def uninitializePlugin(obj):
    """
    Exit point for a plugin
    """
    plugin = om.MFnPlugin(obj)
    try:
        plugin.deregisterNode(AttributeNode.nodeId)
    except:
        om.MGlobal.displayError(
            "Failed to deregister command: {0}".format(AttributeNode.nodeName)
        )


