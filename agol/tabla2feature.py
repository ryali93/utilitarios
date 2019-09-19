#
import arcpy
import os

BDG = r'D:\RYali\TDR5\4product\dgar_solicitudes\BDG.gdb'

tabla_in = os.path.join(BDG, 'Export_Output')
tabla_out = os.path.join(BDG, 'GPO_DGAR_SOLICITUD_3')

arcpy.DeleteRows_management(tabla_out)

cursorI = arcpy.da.InsertCursor(tabla_out, ['SHAPE@', 'ZONA', 'X', 'Y', 'REGION', 'PROVINCIA', 'DISTRITO', 'SEC_OFICIO', 'ANNO', 'FECHA', 'SOLICITANTE', 'OFICIO', 'ASUNTO_DOC', 'SOLICIT_ESTADO', 'INF_ESTADO', 'CODIGO', 'INF_TECNICO', 'PELIGRO', 'AUTOR', 'FECHA_ENTREGA'])
zonas = {'17s': 32717, '18s': 32718, '19s': 32719, '19S': 32719, '17S': 32717}
for z in zonas:
    sql = "ZONA = '%s'"%z
    sr = arcpy.SpatialReference(zonas[z])
    print([x.name for x in arcpy.ListFields(tabla_in)])
    with arcpy.da.SearchCursor(tabla_in, ['X', 'Y', 'ZONA', 'REGION', 'PROVINCIA', 'DISTRITO', 'SEC_OFICIO', 'ANNO', 'FECHA', 'SOLICITANTE', 'OFICIO', 'ASUNTO_DOC', 'SOLICIT_ESTADO', 'INF_ESTADO', 'CODIGO', 'INF_TECNICO', 'PELIGRO', 'AUTOR', 'FECHA_ENTREGA'], sql) as cursorS:
        for s in cursorS:
            punto = arcpy.PointGeometry(arcpy.Point(s[0], s[1]), sr)
            cursorI.insertRow([punto, s[2], s[0], s[1], s[3], s[4], s[5], s[6], s[7], s[8], s[9], s[10], s[11], s[12], s[13], s[14], s[15], s[16], s[17], s[18]])


# with arcpy.da.UpdateCursor('GPO_DGAR_SOLICITUD_2', ['ZONA']) as cursor:
#     for x in cursor:
#         x[0] = x[0][:-1]
#         cursor.updateRow(x)

# with arcpy.da.UpdateCursor('GPO_DGAR_SOLICITUD_2', ['SOLICIT_ESTADO']) as cursor:
#     for x in cursor:
#         if x[0] == 'Por atender':
#             x[0] = '03'
#         elif x[0] == 'En atención' or x[0] == 'En atenci\xf3n' or x[0] == 'En atenci\xf3n ':
#             x[0] = '02'
#         elif x[0] == 'Atendido':
#             x[0] = '01'
#         cursor.updateRow(x)

