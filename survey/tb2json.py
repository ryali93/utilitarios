# encoding=utf8
import json
import os
import arcpy
import pandas as pd

arcpy.env.overwriteOutput  = True

gdb = r'D:\APPS\SURVEY\MG_DGR\SurveyTest.gdb'
path = r'D:\APPS\SURVEY\MG_DGR\tb'

lDom = [x.name for x in arcpy.da.ListDomains(gdb)]

for x in lDom:
    print x
    tbtemp = arcpy.DomainToTable_management(gdb, x, os.path.join(gdb, "tb_%s" % x), "Code", "Desc")
    with arcpy.da.SearchCursor(tbtemp, ["Code", "Desc"]) as cursor:
        for i in cursor:

    # data = arcpy.da.TableToNumPyArray(tbtemp, ["Code", "Desc"])
    # print data
    # df = pd.DataFrame(data)
    # print df
    with open(path + "{}.json".format(x), 'wb') as outfile:
        json.dump(df, outfile)