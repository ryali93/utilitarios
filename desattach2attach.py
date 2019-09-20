import arcpy
from arcpy import da
import os

feature = arcpy.GetParameterAsText(0)
inTable = arcpy.GetParameterAsText(1)
fileLocation = arcpy.GetParameterAsText(2)

with da.SearchCursor(inTable, ['DATA', 'ATT_NAME', 'REL_GLOBALID']) as cursor:
    for item in cursor:
        attachment = item[0]
        filename = str(item[2]) + "_" + str(item[1])
        open(fileLocation + os.sep + filename, 'wb').write(attachment.tobytes())
        del item
        del filename
        del attachment

arcpy.AddField_management(inTable, "NAME_FOTO", "TEXT", "", "", 100)
with arcpy.da.UpdateCursor(inTable, ["NAME_FOTO", "REL_GLOBALID", "ATT_NAME"]) as cursor:
    for x in cursor:
        x[0] = str(x[1]) + "_" + str(x[2])
        cursor.updateRow(x)


arcpy.AddAttachments_management(feature, 
    'GLOBALID', 
    inTable, 
    'REL_GLOBALID', 
    'NAME_FOTO', 
    fileLocation)
