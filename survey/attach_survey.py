from arcpy import da
import arcpy
import os
import subprocess

arcpy.env.workspace = r"D:\APPS\SURVEY\BDG_DGAR_PELIGROS.gdb"
inTable = "TB_PG_FOTOS__ATTACH"

fileLocation = r"D:\APPS\SURVEY\BDG_DGAR_PELIGROS\photos"

with da.SearchCursor(inTable, ['DATA','ATT_NAME','GLOBALID']) as cursor:
    for row in cursor:
        binaryRep = row[0]
        fileName = str(row[2]) + ".jpg"
        open(fileLocation + os.sep + fileName, 'wb').write(binaryRep.tobytes())

        del row
        del binaryRep
        del fileName