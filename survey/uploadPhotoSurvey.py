# -*- coding: utf-8 -*-
#!/usr/local/bin/python27
import io, os
import urllib, urllib2
import arcpy


# with arcpy.da.SearchCursor(tb, ["CODCAL"]) as Cursor:
# 	i = 0
# 	with arcpy.da.InsertCursor("CODCAL", "NOMBRE", "IMAGE") as IsCursor:
# 		for x in Cursor:
# 			i = i + 1
# 			rw[0] = x
# 			rw[1] = x + "-" + i
# 			rw[2] = 
# 			row = []
# 			IsCursor.insertRow(row)

url = u"https://services1.arcgis.com/IOnDXYLCAWAfoO54/ArcGIS/rest/services/service_bf568784c0c24107bdd494850b234f3c/FeatureServer/3/2/attachments/1?token=xsbYmRo9wWeeTVqJfwS0DCD0lmmdD4HXaArRdg3SxBTYgQqdq5v_lqscy3oDtm_2Xu2Q8iTA1OZ2e1pTeqIttdMa3u0lySo7lTg1C9bBRB2xDx6YZeyrEum6JPbKEYvDONzRyxNtuE-JiJQDymj3oky6cgL9LvvngXTKl4S_QgLDY7TKEnmjadCwL-zauR66Y9XAjxU4IIGZ7DIyZCaL3A.."
tb = r'D:\APPS\SURVEY\BDG_DGR_GEOPEDOLOGIA\GPT_MS_POG.gdb\TB_MS_FOTOS'
filedata = urllib2.urlopen(url)
datatowrite = filedata.read()


# f = urllib2.urlopen(url)
# print f
# image_blob = r'D:\APPS\SURVEY\BDG_DGR_GEOPEDOLOGIA\photos\1.jpg'
# jpg = open(f, 'rb').read()
# with arcpy.da.UpdateCursor(tb, ["NOMBRE", "IMAGE"]) as cursor:
#     for row in cursor:  
#         row[0] = "test1"
#         row[1] = jpg
#         cursor.updateRow(row)

i = 0
oc = arcpy.da.InsertCursor(tb, ["NOMBRE", "IMAGE"])
for row in range(2):
    i = i + 1
    a = "test1"
    b = datatowrite
    oc.insertRow([a, b])