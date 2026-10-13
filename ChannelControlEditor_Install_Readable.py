# Channel Control Editor - Simple Maya Drag-and-Drop Installer
# Drag this file into the Maya viewport to add a shelf button.
# All editor code is written as plain Python below (no encoded payload).
# The shelf button is self-contained; no external script path is needed.

import maya.cmds as cmds
import maya.mel as mel

labelName = 'Channel'
annot = 'Channel Control Editor | Show / Hide Transform Channels'
imagePath = 'commandButton.png'
imageLabel = 'Channel'


def createShelfButton():
    shelf = mel.eval('$tmp=$gShelfTopLevel')
    currentShelf = cmds.tabLayout(shelf, q=True, selectTab=True)
    if not currentShelf:
        cmds.warning('Unable to find the current Maya shelf.')
        return

    # This is the actual Python code executed when the shelf button is clicked.
    # You can read and edit the code normally, just like AttributeReset_Install.py.
    command = '''
import maya.cmds as cmds
import maya.mel as mel

def channelWindow():
    if (cmds.window('ChannelCtrl' ,q=True, exists = True)):
        cmds.deleteUI('ChannelCtrl',window=True)
    channel_window = 'ChannelCtrl'
    window_channel = cmds.window(channel_window,t="ChannelBox",widthHeight=(250,230))
    form = cmds.formLayout()
    tabs = cmds.tabLayout()
    form_menu = cmds.formLayout( form ,edit=True ,attachForm=((tabs, 'top', 0),(tabs, 'bottom', 0),(tabs, 'right', 1),(tabs, 'left', 0)) )  
    column_menu =cmds.rowColumnLayout(form_menu,adj=True)
    cmds.tabLayout(tabs,edit=True,tabLabel=(column_menu, 'Channel'))
    formMainForm = cmds.formLayout(numberOfDivisions = 100)
    instruction = cmds.text('=== show tx.ty.tz.rx.ry.rz.sx.sy.sz ===',align="center",en=1,fn='smallPlainLabelFont')
    titleSepTop = cmds.separator(style='in')
    titleSeperatorFirst = cmds.separator(style='in',hr=False,h=120)
    titleSeperatorSec = cmds.separator(style='in')
    
    allTickCheckBox = cmds.checkBox(l='All',v=True,cc=lambda x:allTickFunction(allTickCheckBox,transCheckBox,rotCheckBox,scaleCheckBox,visCheckBox)) 
    transCheckBox = cmds.checkBox(l='translate',v=True)
    rotCheckBox = cmds.checkBox(l='rotate',v=True)
    scaleCheckBox = cmds.checkBox(l='scale',v=True)
    visCheckBox = cmds.checkBox(l='visible',v=True)
    
    textButton = cmds.text('- SELECT -')
    b2 = cmds.button("ShowAttribute",c=lambda x:showAttribute(transCheckBox,rotCheckBox,scaleCheckBox,visCheckBox,lockValue=True,keyValue=True))
    b3 = cmds.button("HideAttribute",c=lambda x:hideAttribute(transCheckBox,rotCheckBox,scaleCheckBox,visCheckBox,lockValue=True,keyValue=True))
    cmds.formLayout(formMainForm, edit=True,attachForm=[(instruction,'left',5),(instruction,'right',5),(instruction,'top',5),
                                                        (titleSepTop,'left',5),(titleSepTop,'right',5),(titleSepTop,'top',25),
                                                        (titleSeperatorFirst,'left',87),(titleSeperatorFirst,'top',28),
                                                        (allTickCheckBox,'left',30),(allTickCheckBox,'right',5),(allTickCheckBox,'top',35),
                                                        (transCheckBox,'left',15),(transCheckBox,'right',5),(transCheckBox,'top',55),
                                                        (rotCheckBox,'left',15),(rotCheckBox,'right',5),(rotCheckBox,'top',75),
                                                        (scaleCheckBox,'left',15),(scaleCheckBox,'right',5),(scaleCheckBox,'top',95),
                                                        (visCheckBox,'left',15),(visCheckBox,'right',5),(visCheckBox,'top',115),
                                                        (textButton,'left',100),(textButton,'right',15),(textButton,'top',36),
                                                        (b2,'left',100),(b2,'right',15),(b2,'top',60),
                                                        (b3,'left',100),(b3,'right',15),(b3,'top',95),
                                                        (titleSeperatorSec,'left',5),(titleSeperatorSec,'right',5),(titleSeperatorSec,'top',152)])
    cmds.showWindow(window_channel)

def allTickFunction(all,trans,rot,scal,vis):
    list = [trans,rot,scal,vis]
    allBox = cmds.checkBox(all,q=True,v=True)
    for each in list:
        if allBox:
            cmds.checkBox(each,e=True,v=True)
        else:
            cmds.checkBox(each,e=True,v=False)

# checkBox tick check
def checkBoxTick(trans,rot,scal,vis):
    list = [trans,rot,scal,vis]
    checkList = []
    for each in list:
        tick = cmds.checkBox(each,q=True,v=True)
        checkList.append(tick)
    return checkList
    
def AttributeCheck(transCheckBox,rotCheckBox,scaleCheckBox,visCheckBox,lockValue=True,keyValue=True):
    checkBoxList = (checkBoxTick(transCheckBox,rotCheckBox,scaleCheckBox,visCheckBox))
    trans,rot,scal,vis = checkBoxList
    selection = cmds.ls(sl=True,type='transform')
    if selection:
        for sel in selection:
            if trans:
                for attr in ['.tx','.ty','.tz']:
                    cmds.setAttr("{}{}".format(sel,attr),lock=lockValue,keyable=keyValue,channelBox=False)
            if rot:
                for attr in ['.rx','.ry','.rz']:
                    cmds.setAttr("{}{}".format(sel,attr),lock=lockValue,keyable=keyValue,channelBox=False)          
            if scal:
                for attr in ['.sx','.sy','.sz']:
                    cmds.setAttr("{}{}".format(sel,attr),lock=lockValue,keyable=keyValue,channelBox=False)      
            if vis:
                for attr in ['.v']:
                    cmds.setAttr("{}{}".format(sel,attr),lock=lockValue,keyable=keyValue,channelBox=False)
    else:
        cmds.warning("NO selection")
            
def hideAttribute(transCheckBox,rotCheckBox,scaleCheckBox,visCheckBox,lockValue=True,keyValue=True):
    AttributeCheck(transCheckBox,rotCheckBox,scaleCheckBox,visCheckBox,lockValue=True,keyValue=False)
    mel.eval('print ("RESULT : attribute < HIDDEN >\\n")')
    
def showAttribute(transCheckBox,rotCheckBox,scaleCheckBox,visCheckBox,lockValue=True,keyValue=True):
    AttributeCheck(transCheckBox,rotCheckBox,scaleCheckBox,visCheckBox,lockValue=False,keyValue=True)
    mel.eval('print ("RESULT : attribute < REVEAL >\\n")')

channelWindow()
'''

    # Update an existing Channel Control button instead of adding duplicates.
    buttons = cmds.shelfLayout(currentShelf, q=True, childArray=True) or []
    for button in buttons:
        if not cmds.shelfButton(button, exists=True):
            continue
        if cmds.shelfButton(button, q=True, annotation=True) == annot:
            cmds.shelfButton(button, e=True, command=command, sourceType='python')
            cmds.warning('Channel Control Editor shelf button updated.')
            return

    cmds.shelfButton(
        parent=currentShelf,
        label=labelName,
        annotation=annot,
        image=imagePath,
        imageOverlayLabel=imageLabel,
        overlayLabelColor=(1, 1, 1),
        overlayLabelBackColor=(0.2, 0.5, 0.9, 0.85),
        command=command,
        sourceType='python'
    )
    cmds.warning('Channel Control Editor installed successfully.')


def onMayaDroppedPythonFile(*args):
    createShelfButton()
    cmds.inViewMessage(
        amg='<hl>Channel Control Editor</hl> installed!',
        pos='topCenter', fade=True
    )


if __name__ == '__main__':
    onMayaDroppedPythonFile()
