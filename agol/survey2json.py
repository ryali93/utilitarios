# -*- coding: utf-8 -*-
import os

ruta = os.path.abspath(os.path.join(__file__, '..'))
lista = [['begin repeat'  , "PADRE"   , "label"], [u'begin group', u'GP_DATOS_PRINC', u'Datos Generales'], [u'select_one 04_DC_Proyecto', u'PROY', u'<i><u><b>Proyecto</b></u></i>'], [u'hidden', u'SUB_PROY', u'<i><u>Subproyecto</u></i>'], [u'text', u'CD_MTRA', u'<i><u>Muestra N\xc2\xb0</u></i>'], [u'datetime', u'F_MTRA', u'<i><u>Fecha</u></i>'], [u'select_one 00_DC_User', u'COLECTADO', u'<i><u>Responsable</u></i>'], [u'select_one 04_DC_MineralDeposito', u'CAT', u'<i><u>Categor\xc3\xada</u></i>'], [u'text', u'OTR_CAT', u'<i><u>Otra Categor\xc3\xada</u></i>'], [u'select_one 04_DC_MinaEstado', u'EST_MIN', u'<i><u>Estado actual</u></i>'], [u'text', u'A_ITS', u'<i><u>Nombre del \xc3\xa1rea de inter\xc3\xa9s</u></i>'], [u'hidden', u'REGISTRO', u'REGISTRO'], [u'end group', None, None], [u'begin group', u'GP_DATOS_UBIC', u'Datos de Ubicaci\xc3\xb3n'], [u'geopoint', u'UBIC', u'<i><u>Ubicaci\xc3\xb3n</u></i>'], [u'hidden', u'LATITUD', u'<i><u>Latitud (\xc2\xb0)</u></i>'], [u'hidden', u'LONGITUD', u'<i><u>Longitud (\xc2\xb0)</u></i>'], [u'integer', u'ESTE', u'<i><u>Este</u></i>'], [u'integer', u'NORTE', u'<i><u>Norte</u></i>'], [u'select_one 04_DC_Datum', u'DATUM', u'<i><u>Datum</u></i>'], [u'select_one 04_DC_Zona', u'ZONA', u'<i><u>Zona</u></i>'], [u'integer', u'ALTITUD', u'<i><u>Altitud</u></i>'], [u'hidden', u'REGION', u'Regi\xc3\xb3n'], [u'hidden', u'PROVINCIA', u'Provincia'], [u'hidden', u'DISTRITO', u'Distrito'], [u'hidden', u'HOJA', u'Cuadr\xc3\xa1ngulo'], [u'hidden', u'T_YACIMIENTO', u'Tipo Yacimiento'], [u'hidden', u'ST_YACIMIENTO', u'Sub-tipo Yacimiento'], [u'end group', None, None], [u'begin repeat', u'TB_RM_LITOLOGIA', u'<font color="blue"><u><i>Litolog\xc3\xada</u></i></font>'], [u'hidden', u'CDMTRA_MN', u'Muestra'], [u'begin group', u'GP_ROCA_HOSPEDANTE', u'Roca Hospedante'], [u'select_one 04_DC_RocaTipo', u'T_ROCA', u'<i><u>Tipo de roca</u></i>'], [u'select_one 04_DC_RocaSubTipo', u'ST_ROCA', u'<i><u>Subtipo de roca</u></i>'], [u'select_one 04_DC_Roca', u'ROCA_MINERAL', u'<i><u>Roca</u></i>'], [u'text', u'GEOMETRIA', u'<i><u>Geometr\xc3\xada</u></i>'], [u'text', u'TEXTURA', u'<i><u>Textura</u></i>'], [u'text', u'U_LITOESTRAT', u'<i><u>Unidad Litoestratigrafica</u></i>'], [u'end group', None, None], [u'begin repeat', u'TB_RM_CARACTMIN_ALTER', u'Caracter\xc3\xadticas de Alteraci\xc3\xb3n'], [u'hidden', u'CDMTRA_MN_A', u'Muestra'], [u'select_one 04_DC_Alteracion', u'ALTERACION', u'<i><u>Alteraciones</u></i>'], [u'select_one 04_DC_AlteracionIntensidad', u'INTENSIDAD', u'<i><u>Intensidad</u></i>'], [u'select_one 04_DC_AlteracionGrupo', u'GRUPO_ALTR', u'<i><u>Grupo</u></i>'], [u'select_one 04_DC_AlteracionMineral', u'MINERAL', u'<i><u>Minerales</u></i>'], [u'select_multiple 04_DC_AlterEstilo', u'E_ALTERACION', u'<i><u>Estilo de Alteraci\xc3\xb3n</u></i>'], [u'hidden', u'ORDEN1', u'ORDEN'], [u'end repeat', None, None], [u'begin group', u'GP_YACIMIENTO', u'Caracter\xc3\xadsticas del Yacimiento'], [u'select_one 04_DC_YacimTipo', u'DEPOSITO', u'<i><u>Tipo de yacimiento</u></i>'], [u'select_one 04_DC_YacimSubtipo', u'ST_DEPOSITO', u'<i><u>Subtipo dep\xc3\xb3sito</u></i>'], [u'select_multiple 04_DC_Mineral', u'MENA', u'<i><u>Mena</u></i>'], [u'select_multiple 04_DC_Mineral', u'GANGA', u'<i><u>Ganga</u></i>'], [u'end group', None, None], [u'end repeat', None, None], [u'begin repeat', u'TB_RM_MINERALIZACION', u'<font color="blue"><u><i>Mineralizaci\xc3\xb3n</i></font>'], [u'hidden', u'CDMTRA_MR', u'Muestra'], [u'text', u'CONTENIDO_MIN', u'<i><u>Contenido (%)</u></i>'], [u'text', u'MINMENA', u'<i><u>Minerales en mena</u></i>'], [u'text', u'MINGANGA', u'<i><u>Gangas</u></i>'], [u'select_one 04_DC_AlterEstilo', u'ESTILO_MIN', u'<i><u>Estilo de mineralizacion</u></i>'], [u'begin repeat', u'TB_RM_MINERALIZACION_ESTR', u'Estructura de mineralizacion'], [u'hidden', u'CDMTRA_MRE', u'Muestra'], [u'hidden', u'ORDEN_ESTR', None], [u'select_one 04_DC_MinerTipo', u'TIPO', u'<i><u>Tipo de estructura</u></i>'], [u'select_one 04_DC_MinerSubtipo', u'SUBTIPO', u'<i><u>Subtipo de estructura</u></i>'], [u'decimal', u'AZIMUT', u'<i><u>Azimut (\xc2\xb0)</u></i>'], [u'integer', u'RUMBO', u'<i><u>Rumbo</u></i>'], [u'select_one 04_DC_Direccion', u'D_RUMBO', u'<i><u>Direcci\xc3\xb3n de rumbo (\xc2\xb0)</u></i>'], [u'integer', u'BUZAMIENTO', u'<i><u>Buzamiento</u></i>'], [u'select_one 04_DC_Direccion', u'D_BUZAMIENTO', u'<i><u>Direcci\xc3\xb3n de buzamiento (\xc2\xb0)</u></i>'], [u'integer', u'PLUNGE', u'<i><u>Plunge</u></i>'], [u'select_one 04_DC_Direccion', u'D_PLUNGE', u'<i><u>Direcci\xc3\xb3n de plunge (\xc2\xb0)</u></i>'], [u'integer', u'PITCH', u'<i><u>Pitch</u></i>'], [u'select_one 04_DC_Direccion', u'D_PITCH', u'<i><u>Direcci\xc3\xb3n de pitch (\xc2\xb0)</u></i>'], [u'text', u'OBSERVACION', u'<i><u>Comentario</u></i>'], [u'end repeat', None, None], [u'end repeat', None, None], [u'begin repeat', u'TB_RM_ACTMINERA', u'<font color="blue"><u><i>Actividad Minera</i></font>'], [u'hidden', u'CDMTRA_AM', u'Muestra'], [u'text', u'ACT_PRD', u'<i><u>Producci\xc3\xb3n</u></i>'], [u'select_one 04_DC_MinaEscala', u'ACT_SC_PRD', u'<i><u>Escala Producci\xc3\xb3n</u></i>'], [u'text', u'ACT_RR_RSV', u'<i><u>Recursos y/o reservas</u></i>'], [u'text', u'ACT_DATO', u'<i><u>Datos empresa</u></i>'], [u'end repeat', None, None], [u'begin repeat', u'TB_RM_TIPOMUESTRA', u'<font color="blue"><u><i>Tipo de muestras</i></font>'], [u'hidden', u'CDMTRA_TM', u'Muestra'], [u'select_one 04_DC_MtraTipo', u'T_MTRA', u'<i><u>Tipo de muestra</u></i>'], [u'text', u'OTR_MTRA', u'<i><u>Otro tipo de muestra</u></i>'], [u'text', u'DSCP_MTRA', u'<i><u>Descripci\xc3\xb3n de muestra</u></i>'], [u'select_one 04_DC_MtreoTipo', u'T_MTRO', u'<i><u>Tipo de muestreo</u></i>'], [u'text', u'OTR_MTRO', u'<i><u>Otro tipo de muestreo</u></i>'], [u'text', u'DSCP_MTRO', u'<i><u>Descripci\xc3\xb3n de muestreo</u></i>'], [u'select_multiple 04_DC_AnalisisMuestraGqm', u'ANA_GEOQ', u'<i><u>An\xc3\xa1lisis geoqu\xc3\xadmico</u></i>'], [u'select_multiple 04_DC_AnalisisMuestraPt', u'ANA_PETRO', u'<i><u>Petromineralogico</u></i>'], [u'select_multiple 04_DC_AnalisisMuestraOt', u'ANA_OTROS', u'<i><u>Otros</u></i>'], [u'select_multiple 04_DC_AnalisisMuestra', u'ANA_EESP', u'<i><u>Estudios especiales</u></i>'], [u'end repeat', None, None], [u'hidden', u'OC_LABO', u'Ocultar laboratorio'], [u'begin repeat', u'TB_RM_LABORATORIO', u'<font color="blue"><u><i>Resultado Laboratorio</i></font>'], [u'hidden', u'CDMTRA_LB', u'Muestra'], [u'hidden', u'ORDEN_LB', u'Orden'], [u'text', u'TIPO_A', u'Tipo'], [u'text', u'ELEMENTO', u'Elemento'], [u'text', u'UNIDAD', u'Unidad'], [u'text', u'SIMBOLO', u'Simbolo'], [u'decimal', u'VALOR', u'Valor'], [u'end repeat', None, None], [u'begin repeat', u'TB_RM_MULTIMEDIA', u'<font color="blue"><u><i>Multimedia</u></i></font>'], [u'hidden', u'CDMTRA_FT', u'Unidad'], [u'image', u'ARCHIVO', u'<i><u>Archivo</u></i>'], [u'text', u'TITULO', u'<i><u>T\xc3\xadtulo</u></i>'], [u'date', u'FECHA', u'<i><u>Fecha</u></i>'], [u'text', u'AUTOR', u'<i><u>Autor</u></i>'], [u'select_one 04_DC_Multimedia', u'TIPO_F', u'<i><u>Tipo Archivo</u></i>'], [u'text', u'DSCP', u'<i><u>Descripci\xc3\xb3n</u></i>'], [u'text', u'OBS', u'<i><u>Observaci\xc3\xb3n</u></i>'], [u'hidden', u'EXT_ARCH', u'Extensi\xc3\xb3n Archivo'], [u'hidden', u'ORDEN', u'Orden'], [u'text', u'LINK', u'Link'], [u'end repeat', None, None], [u'audio', u'AUDIO', u'<i><u>Audio</u></i>'], ["end repeat"    , "FINAL"   , "label"]]



def createJSONFeature(ruta, lista):
    prev_a = ""
    count = 1
    diccio = {}

    for i in lista:
        if i[0] == "begin repeat" and prev_a == "":
            js        = os.path.join(ruta, i[1] + ".json")
            f         = open(js, "wb")
            act       = f
            diccio[1] = f
        if i[0] == "begin repeat" and prev_a == "begin repeat":
            jg        = os.path.join(ruta, i[1] + ".json")
            g         = open(jg, "wb")
            act       = g
            diccio[2] = g
        if i[0] == "begin repeat" and prev_a == "begin repeatbegin repeat":
            jh        = os.path.join(ruta, i[1] + ".json")
            h         = open(jh, "wb")
            act       = h
            diccio[3] = h
        if i[0] == "begin repeat" and prev_a == "begin repeatbegin repeatbegin repeat":
            jk        = os.path.join(ruta, i[1] + ".json")
            k         = open(jk, "wb")
            act       = k
            diccio[4] = k

        if i[0] == "begin repeat":
            prev_a    += i[0]
        elif i[0] == "end repeat":
            prev_a    = prev_a[:-12]
        else:
            prev_a    = prev_a

        if i[0] == "end repeat":
            act.close()
            act = diccio.get(len(prev_a)/12)

        if i[0] not in ["begin repeat", "end repeat"]:
            # act.write('{}\n'.format(str(i)))
            print i
            act.write(template(i))
        count += 1


def template(x):
    texto2 = ""
    if x[0] == "integer":
        texto2 = u'{ "alias": "{}", "name": "{}", "type": "esriFieldTypeInteger"}'.format(x[2], x[1])
    elif x[0] == "decimal":
        texto2 = u'{ "alias": "{}", "name": "{}", "type": "esriFieldTypeDouble"}'.format(x[2], x[1])

    elif x[0] in ["date"]:
        texto2 = u'{ "alias": "{}", "length": 8, "name": "{}",  "type": "esriFieldTypeDate"}'.format(x[2], x[1])

    elif x[0] in ["audio", "image"]:
        texto2 = u'{ "alias": "{}", "length": 255, "name": "{}",  "type": "esriFieldTypeString"}'.format(x[2], x[1])

    elif x[0] in ["geopoint", "end group"]:
        pass

    elif type(x[0])=="str":
        if x[0] in ["text", "hidden"] or x[0].split(" ")[0] in ["select_one", "select_multiple"]:
            texto2 = u'{"alias": "{}", "length": 255, "name": "{}",  "type": "esriFieldTypeString"}'.format(x[2], x[1])
        elif x[0].split(" ")[0] == "begin group":
            pass
    return texto2

createJSONFeature(ruta, lista)