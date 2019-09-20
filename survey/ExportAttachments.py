import arcpy
import os

# inTable = r'D:\APPS\SURVEY\BDG_DGR_GEOPEDOLOGIA\GPT_MS_POG.gdb\TB_MS_FOTOS'

inTable = r'C:\Users\autonomoosi02\AppData\Local\Temp\scratch.gdb\TB_MS_FOTOSac651c'
fileLocation = r'D:\APPS\SURVEY\BDG_DGR_GEOPEDOLOGIA\photos'

i = 0
with arcpy.da.SearchCursor(inTable, ['IMAGE', 'TITULO']) as cursor:
    for item in cursor:
        i=i+1
        attachment = item[0]
        if attachment is not None:
            print attachment
            if item[1] != None:
                filename = item[1] + str(i) + ".jpg"
            else:
                filename = str(i) + ".jpg"
            open(fileLocation + os.sep + filename, 'wb').write(attachment.tobytes())
            del item
            del filename
            del attachment
