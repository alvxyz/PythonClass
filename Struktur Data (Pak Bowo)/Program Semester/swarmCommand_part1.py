# swarmCommand_part1.py

import sys
import random
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx
import maya.OpenMayaFX as OpenMayaFX

# The name of the command.
commandName = 'swarm'


# ===============================================
# Class Definition.
# ===============================================

class SwarmCommand(OpenMayaMPx.MPxCommand):
    # Maintain a counter to identify the number of particle swarms created.
    instanceId = 0

    # Default values.
    default_numParticles = 50
    default_dimensions = (5, 5, 5)

    def __init__(self):
        ''' Constructor. '''
        OpenMayaMPx.MPxCommand.__init__(self)

        # Give a unique name to this command instance.
        self.instanceName = commandName + str(SwarmCommand.instanceId)
        SwarmCommand.instanceId += 1

        # Particle system instance variables
        self.particleSystemName = self.instanceName + '_Particles'
        self.numParticles = SwarmCommand.default_numParticles
        self.particlePositions = OpenMaya.MPointArray()

        # Turbulence field instance variables
        self.turbulenceFieldName = self.instanceName + '_Turbulence'
        self.size_x = SwarmCommand.default_dimensions[0]
        self.size_y = SwarmCommand.default_dimensions[1]
        self.size_z = SwarmCommand.default_dimensions[2]

        self.dagModifier = OpenMaya.MDagModifier()

    def isUndoable(self):
        ''' Determines whether or not this command is undoable within Maya. '''
        return True

    def doIt(self, args):
        ''' Command's first-time execution. '''

        # Clear the current selection list to avoid any wrong grouping.
        OpenMaya.MGlobal.clearSelectionList()

        # Create the turbulence field
        self.dagModifier.commandToExecute('turbulence -name "' + self.turbulenceFieldName + '"')
        self.dagModifier.commandToExecute('scale ' + str(0.5 * self.size_x) + ' '
                                          + str(0.5 * self.size_y) + ' '
                                          + str(0.5 * self.size_z) + ' '
                                          + self.turbulenceFieldName)
        self.dagModifier.commandToExecute(
            'setAttr "' + self.turbulenceFieldName + '.volumeShape" 1')  # 1 for cube, 2 for sphere.
        self.dagModifier.commandToExecute('setAttr "' + self.turbulenceFieldName + '.magnitude" 100')
        self.dagModifier.commandToExecute('setAttr "' + self.turbulenceFieldName + '.attenuation" 0.1')
        self.dagModifier.commandToExecute('setAttr "' + self.turbulenceFieldName + '.frequency" 4')
        self.dagModifier.commandToExecute('setAttr "' + self.turbulenceFieldName + '.interpolationType" 1')
        self.dagModifier.commandToExecute('setAttr "' + self.turbulenceFieldName + '.noiseLevel" 8')
        self.dagModifier.commandToExecute('setAttr "' + self.turbulenceFieldName + '.noiseRatio" 1')
        self.dagModifier.commandToExecute('setAttr "' + self.turbulenceFieldName + '.trapInside" 1')
        self.dagModifier.commandToExecute('setAttr "' + self.turbulenceFieldName + '.trapRadius" 1')

        # Create the particle system
        self.dagModifier.commandToExecute('particle -name "' + self.particleSystemName + '"')
        self.dagModifier.commandToExecute('setAttr "' + self.particleSystemName + 'Shape.conserve" 0.75')
        self.dagModifier.commandToExecute(
            'setAttr "' + self.particleSystemName + 'Shape.particleRenderType" 6')  # 3 for points, 6 for streaks

        # Connect the particle system to the turbulence field.
        self.dagModifier.commandToExecute(
            'connectDynamic -f ' + self.turbulenceFieldName + ' ' + self.particleSystemName + 'Shape')

        # Execute the commands enqueued in the MDagModifier.
        self.dagModifier.doIt()

        # Call a helper function to obtain the MDagPath of the shape.
        particleShapeDagPath = self.getDagPathToObject(self.particleSystemName + 'Shape')

        # Create a function set around the particleShapeDagPath.
        particleSystemFn = OpenMayaFX.MFnParticleSystem(particleShapeDagPath)

        # Randomly generate the positions of the particles within the volume.
        for i in range(0, self.numParticles):
            self.particlePositions.append(random.uniform(0.5 * -self.size_x, 0.5 * self.size_x),
                                          random.uniform(0.5 * -self.size_y, 0.5 * self.size_y),
                                          random.uniform(0.5 * -self.size_z, 0.5 * self.size_z))

        # Emit particles using the particle positions.
        particleSystemFn.emit(self.particlePositions)

        # Save the starting positions of the particles, so we can scrub the timeline.
        particleSystemFn.saveInitialState()

    def redoIt(self):
        ''' Re-do the work of the command. '''
        self.dagModifier.doIt()

    def undoIt(self):
        ''' Undo the work performed by the command. '''
        self.dagModifier.undoIt()

    def getDagPathToObject(self, objectName):
        ''' Returns the DAG path to the specific shape name '''
        selectionList = OpenMaya.MSelectionList()
        OpenMaya.MGlobal.getSelectionListByName(objectName, selectionList)
        dagPath = OpenMaya.MDagPath()
        selectionList.getDagPath(0, dagPath)
        return dagPath

    # ===============================================


# Plug-in Initialization.
# ===============================================


def cmdCreator():
    ''' Return an instance of the command. '''
    return OpenMayaMPx.asMPxPtr(SwarmCommand())


def initializePlugin(mobject):
    ''' Initialize the plug-in when Maya loads it. '''
    plugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        plugin.registerCommand(commandName, cmdCreator)
    except:
        sys.stderr.write('Failed to register command: ' + commandName)


def uninitializePlugin(mobject):
    ''' Uninitialize the plug-in when Maya un-loads it. '''
    plugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        plugin.deregisterCommand(commandName)
    except:
        sys.stderr.write('Failed to unregister command: ' + commandName)


# ===============================================
# Sample Usage.
# ===============================================
''' 
# Copy the following lines and run them in Maya's Python Script Editor:

import maya.cmds as cmds
cmds.swarm()
'''
