import sys
import arcpy
import json

jsonFile = r'C:\Users\autonomoosi02\Desktop\Ccarga.json'
with open(jsonFile, "r") as f:
    jx=f.read().decode("Windows-1252")
    data = json.loads(jx)
df = arcpy.AsShape(data)
print df