# encoding=utf8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import sqlite3
import json
import csv
import os
import uuid
# import arcpy
import itertools

dbname = arcpy.GetParameterAsText(0)
folder = arcpy.GetParameterAsText(1)

# dbname = r"D:\APPS\SQLITE\Bug\a084e65cd9403d813e8ec667ca329a63.sqlite"
# folder = r"D:\APPS\SQLITE\Bug"

conn = sqlite3.connect(dbname)
cur = conn.cursor()
sql = "select * from Surveys LIMIT 93;"

cur.execute(sql)

info = [x for x in cur]
# info = []

# for x in cur:
#     try:
#         print info
#         info.append(x)
#     except Exception as e:
#         pass
    

table_name = {k: list() for k in list(set([x[0] for x in info]))}

LISTANOMBRES=[]
abc = list(set([x[6] for x in info]))
for i in abc:
    abcd = [k for k,v in json.loads(i).items()]
    LISTANOMBRES.append(abcd[0])
table_name = {k:list() for k in list(set(LISTANOMBRES))}


for x in info:
    data = json.loads(x[6])
    for k, v in data.items():
        table_name[k].append(v)



listaForm = []
for k, val in table_name.items():
    listaForm.append(k)


for f in listaForm:
    ui = str(uuid.uuid4())
    path_txt = os.path.join(folder, '{}{:.3}.txt'.format(f,ui))
    path_csv = os.path.join(folder, '{}{:.3}.csv'.format(f,ui))

    keys = []
    rows = []
    for k, v in table_name.items():
        if k == f:
            for i in v:
                keys.append(list(i))
                rows.append(i)

    LL = set(itertools.chain.from_iterable(keys))

    for n in LL:
        components = [x for x in keys if n in x]
        for i in components:
            keys.remove(i)
        keys += [list(set(itertools.chain.from_iterable(components)))]

    keys = keys[0]

    with open(path_txt, 'w') as f:
        llave = ''
        for nn in keys:
            llave += '%s|' % nn
        f.write(llave)
        f.write('\n')
        for i in rows:
            registro = str()
            for k in keys:
                registro += '%s|' % i.get(k)

            f.write(registro)
            f.write('\n')

        f.close()

    in_txt = csv.reader(open(path_txt, "rb"), delimiter = '|')
    out_csv = csv.writer(open(path_csv, 'wb'))

    out_csv.writerows(in_txt)

