import io
import os
import cx_Oracle
import urllib, urllib2

image_blob = r'D:\APPS\SURVEY\BDG_DGR_GEOPEDOLOGIA\photos\1.jpg'
jpg = open(image_blob, 'rb').read()

def conn():
    inst = "bdgeocat"
    user_sde = "bdtecnica"
    password_sde = "bdtecnica"
    connect = cx_Oracle.connect(user_sde, password_sde, inst)
    return connect
conexion = conn()
cursor = conexion.cursor()

my_blob = cursor.var(cx_Oracle.BLOB)
my_blob.setvalue(0, jpg)

cursor.execute("INSERT INTO DATA_EDIT.TB_MS_FOTOS (NOMBRE, IMAGE) VALUES ('1', %s);" % my_blob)
conexion.commit()
conexion.close()
