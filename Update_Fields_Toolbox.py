# This ArcPy tool updates feature classes in a specified target database by executing a Python script file(.py).

import arcpy
import os
import sys

class Toolbox(object):
    def __init__(self):
        self.label = "Update Feature Classes Toolbox"
        self.alias = "UpdateFC"
        self.tools = [UpdateFeatureClassesTool]

class UpdateFeatureClassesTool(object):
    def __init__(self):
        self.label = "Update Feature Classes"
        self.description = "Update feature classes based on a script and geodatabase"
        self.canRunInBackground = False

    def getParameterInfo(self):
        # Define parameters
        params = []

        param0 = arcpy.Parameter(
            displayName="Script File",
            name="script_file",
            datatype="DEFile",
            parameterType="Required",
            direction="Input"
        )
        params.append(param0)

        param1 = arcpy.Parameter(
            displayName="Geodatabase",
            name="geodatabase",
            datatype="DEWorkspace",
            parameterType="Required",
            direction="Input"
        )
        params.append(param1)

        return params

    def isLicensed(self):
        return True

    def updateParameters(self, parameters):
        return

    def updateMessages(self, parameters):
        return

    def execute(self, parameters, messages):
        script_file = parameters[0].valueAsText
        geodatabase = parameters[1].valueAsText

        # Set the workspace to the provided geodatabase
        arcpy.env.workspace = geodatabase

        # Import the script
        script_dir, script_name = os.path.split(script_file)
        script_name = os.path.splitext(script_name)[0]

        # Add the script directory to the system path
        sys.path.insert(0, script_dir)

        try:
            script_module = __import__(script_name)
        except ModuleNotFoundError as e:
            arcpy.AddError(f"Error importing script: {e}")
            raise

        # Call the main function from the imported script module
        if hasattr(script_module, 'main'):
            script_module.main()
        else:
            arcpy.AddError("The script does not contain a 'main' function.")

        return
