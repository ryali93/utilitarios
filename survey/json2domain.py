#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import arcpy
import os
import pandas as pd
import json
reload(sys)
sys.setdefaultencoding('Windows-1252')

gdb = r"D:\APPS\SURVEY\BDG_DGAR_FAGUA\BDG_DGAR_FAGUA.gdb"
pathjson = r'D:\APPS\SURVEY\BDG_DGAR_FAGUA\json'
pathDom = os.path.join(pathjson, "domain")
listpaths = [os.path.join(pathDom, x) for x in os.listdir(pathDom)]

def makeDomain(jsonFile):
    with open(jsonFile, "r") as f:
        jx=f.read().decode("Windows-1252")
        df = pd.read_json(jx)
    domain = arcpy.CreateDomain_management(gdb, df["name"][0], '', 'TEXT')
    for dom in df['codedValues']:
        val = [v for k,v in dom.items()]
        print val
        arcpy.AddCodedValueToDomain_management(gdb, df['name'][0], val[0], val[1])

def main():
    for i in listpaths:
        print i
        makeDomain(i)

if __name__ == '__main__':
    main()