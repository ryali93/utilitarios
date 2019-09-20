#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
from dbfpy import dbf
import os
import sys

filename = r'D:\temp\SHP\planta.dbf' # Cambiar la ruta


if filename.endswith('.dbf'):
    print "Convirtiendo %s a csv" % filename
    csv_fn = filename[:-4]+ ".txt"
    with open(csv_fn,'wb') as csvfile:
        in_db = dbf.Dbf(filename)
        out_csv = csv.writer(csvfile)
        names = []
        for field in in_db.header.fields:
            names.append(field.name)
        out_csv.writerow(names)
        for rec in in_db:
            out_csv.writerow(rec.fieldData)
        in_db.close()
        print "Holi..."


path_csv = r'D:\temp\SHP\planta.csv'
in_txt = csv.reader(open(csv_fn, "rb"), delimiter = ',')
out_csv = csv.writer(open(path_csv, 'wb'))
out_csv.writerows(in_txt)
