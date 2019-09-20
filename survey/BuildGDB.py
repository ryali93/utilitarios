#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import arcpy
import os
import uuid
import pandas as pd
import json
reload(sys)
sys.setdefaultencoding('Windows-1252')
# sys.setdefaultencoding("utf-8")


arcpy.env.overwriteOutput = True
# BASE_DIR = arcpy.GetParameterAsText(0)
# MODULE_NAME = arcpy.GetParameterAsText(1)

BASE_DIR = r"D:\APPS\SURVEY\BDG_DGAR_FASUB"
MODULE_NAME = "BDG_DGAR_FASUB"
# x[0] = NOMBRE , x[1] = GDB
# listFieldsDomain = ["AGRIET","04_DC_Agrietamiento"], ["AGUASUB","04_DC_AguaSubPresencia"], ["ESTILO","04_DC_EscarpaEstilo"], ["PG_FACTANT","04_DC_PG_FactAntropico"], ["PG_FACTEG","04_DC_PG_FactEntornoGeog"], ["PG_FACTSIT","04_DC_PG_FactSitio"], ["PROCGEOLANT","04_DC_ProcGeolAntiguo"], ["LITOLOGIA","04_DC_TipoRoca"], ["VEGTIPO","04_DC_VegetacionTipo"], ["RESPONS","00_DC_User"], ["ESTADO","04_DC_ActivEstado"], ["AGUASUBCAR","04_DC_AguaSubCaract"], ["GRADOALT","04_DC_AlteracionGrado"], ["ALUD","04_DC_Alud"], ["AREAINUN","04_DC_AreaInundable"], ["CARACTAREN","04_DC_ArenamientoCaract"], ["EFECTAREN","04_DC_ArenamientoEfecto"], ["VOLCARRQ","04_DC_Arranque"], ["CAIDARRQ","04_DC_Arranque"], ["CURSORIO","04_DC_CursoRio"], ["DANO","04_DC_DanoCaract"], ["VOLCDPCAR","04_DC_DepositoCaract"], ["CAIDDPCAR","04_DC_DepositoCaract"], ["DEPSUPERF","04_DC_DepositoSuperficial"], ["DISCONROCA","04_DC_DiscontinuidadRoca"], ["FENOMEDAD","04_DC_EdadEstimada"], ["EDAD","04_DC_EdadFenom"], ["EMBANT","04_DC_EmbalseAntiguo"], ["ESTEVOL","04_DC_ErosionEstEvol"], ["EROFLUV","04_DC_ErosionFluvial"], ["TIPOERO","04_DC_ErosionLadera"], ["ZONAINV","04_DC_ErosionZonaInvol"], ["DISTRIB","04_DC_EscarpaDistribucion"], ["ESCARPFORM","04_DC_EscarpaForma"], ["SUPERF","04_DC_EscarpaSuperficie"], ["FLUJEF","04_DC_FlujoEfectos"], ["FLUJFORM","04_DC_FlujoForma"], ["FLUJOMAT","04_DC_FlujoMaterial"], ["VOLCFZONA","04_DC_FormaArranque"], ["CAIDFZONA","04_DC_FormaArranque"], ["FORMTERR","04_DC_FormaTerreno"], ["VOLCROTU","04_DC_Fracturamiento"], ["CAIDROTU","04_DC_Fracturamiento"], ["FTEINFO","04_DC_FteInformacion"], ["PELIGRO","04_DC_GradoPeligro"], ["VULNER","04_DC_GradoVulnerabilidad"], ["HUNDIM","04_DC_Hundimiento"], ["INTENSFRAC","04_DC_IntensidadFracturam"], ["LADERA","04_DC_Ladera"], ["LATENTE","04_DC_Latente"], ["MMASAEST","04_DC_MovMasaEstado"], ["MMASAINF","04_DC_MovMasaInferido"], ["MMASATIPO","04_DC_MovMasaTipo"], ["PELIGTIPO","04_DC_PeligroTipo"], ["PELIGNOM","04_DC_PeligroTipoEspecial"], ["PENDIENTE","04_DC_Pendiente"], ["PLANICIE","04_DC_Planicie"], ["RECURPEL","04_DC_RecurrenciaPeligro"], ["REPTACION","04_DC_Reptacion"], ["GRADOSAT","04_DC_SaturacionGrado"], ["SUELCOHE","04_DC_SueloCohesivo"], ["SUELOGRAN","04_DC_SueloGranular"], ["VOLCTALUD","04_DC_Talud"], ["CAIDTALUD","04_DC_Talud"], ["USOTERRMAR","04_DC_UsoErosionFluvial"], ["USOTERRFLU","04_DC_UsoErosionFluvial"], ["USOTERR","04_DC_UsoTerreno"], ["USOINUN","04_DC_UsoTerrenoInundacion"], ["VALLE","04_DC_Valle"], ["VEGDENS","04_DC_VegetacionDensidad"], ["VELMOV","04_DC_Velocidad"], ["ZONA","04_DC_Zona"]
# listFieldsDomain = ["ELEMPRIN","04_DC_Elemento"], ["ELEMACOM","04_DC_Elemento"], ["MENA","04_DC_Mineral"], ["YM_MINTIPO","04_DC_YM_MineriaTipo"], ["YM_YMSTIPO","04_DC_YM_YacMetalicoSubtipo"], ["DATUM","04_DC_Datum"], ["RESP","00_DC_User"], ["REV","00_DC_User"], ["ZONA","04_DC_Zona"], ["ALTERGPO","04_DC_AlteracionGrupo"], ["ALTERINT","04_DC_AlteracionIntensidad"], ["ALTERMINER","04_DC_AlteracionMineral"], ["ALTHIDROT","04_DC_AlteracionHidrotermal"], ["DOMGEOTEC","04_DC_DomGeotectonico"], ["ELEMMET","04_DC_Elemento"], ["MIN_UCFINO","04_DC_MinUnidContFino"], ["MIN_UPESO","04_DC_MinUnidPeso"], ["MINAESCALA","04_DC_MinaEscala"], ["MINAESTADO","04_DC_MinaEstado"], ["GANGA","04_DC_Mineral"], ["MINERGEOC","04_DC_MineralGeocron"], ["ROCA","04_DC_Roca"], ["ROCASTIPO","04_DC_RocaSubtipo"], ["ROCATIPO","04_DC_RocaTipo"], ["SISTFALLA","04_DC_SistemaFallas"], ["UGEOLOGICA","04_DC_UnidGeologica"], ["YM_CALIDAD","04_DC_YM_Calidad"], ["YM_GEOCRON","04_DC_YM_Geocron"], ["YM_GEOMET","04_DC_YM_Estilo"], ["YM_METDAT","04_DC_YM_MetodoDatacion"], ["YM_REFWEB","04_DC_YM_ReferenciaWeb"], ["YM_RMTIPO","04_DC_YM_RecursoMineralTipo"], ["YM_RVATIPO","04_DC_YM_ReservaTipo"], ["YM_TIPO","04_DC_YM_Tipo"], ["YM_ULEY","04_DC_YM_UnidLey"], ["YM_YMTIPO","04_DC_YM_YacimientoTipo"] 
# listFieldsDomain = ["E_ALTERACION", "04_DC_AlterEstilo"], ["ANA_EESP", "04_DC_AnalisisMuestra"], ["ANA_GEOQ", "04_DC_AnalisisMuestraGqm"], ["ANA_OTROS", "04_DC_AnalisisMuestraOt"], ["ANA_PETRO", "04_DC_AnalisisMuestraPt"], ["MENA", "04_DC_Mineral"], ["GANGA", "04_DC_Mineral"], ["COLECTADO", "00_DC_User"], ["ALTERACION", "04_DC_Alteracion"], ["GRUPO_ALTR", "04_DC_AlteracionGrupo"], ["INTENSIDAD", "04_DC_AlteracionIntensidad"], ["MINERAL", "04_DC_AlteracionMineral"], ["ESTILO_MIN", "04_DC_AlterEstilo"], ["DATUM", "04_DC_Datum"], ["R_RUMBO", "04_DC_Direccion"], ["D_BUZAMIENTO", "04_DC_Direccion"], ["D_PLUNGE", "04_DC_Direccion"], ["D_PITCH", "04_DC_Direccion"], ["ACT_SC_PRD", "04_DC_MinaEscala"], ["EST_MIN", "04_DC_MinaEstado"], ["CAT", "04_DC_MineralDeposito"], ["SUBTIPO", "04_DC_MinerSubtipo"], ["TIPO", "04_DC_MinerTipo"], ["T_MTRA", "04_DC_MtraTipo"], ["T_MTRO", "04_DC_MtreoTipo"], ["TIPO_F", "04_DC_Multimedia"], ["PROY", "04_DC_Proyecto"], ["ROCA_MINERAL", "04_DC_Roca"], ["ST_ROCA", "04_DC_RocaSubTipo"], ["T_ROCA", "04_DC_RocaTipo"], ["ST_DEPOSITO", "04_DC_YacimSubtipo"], ["DEPOSITO", "04_DC_YacimTipo"], ["ZONA", "04_DC_Zona"]
listFieldsDomain = ["00_DC_User", "USUARIO"], ["04_DC_FA_Analisis", "ANALISIS"], ["04_DC_RocaTipo", "T_ROCA"], ["04_DC_UsoAgua", "USO"], ["00_DC_User", "COLECTADO"], ["04_DC_AguaSubterranea", "AGUA_SUB"], ["04_DC_AguaSuperficial", "AGUA_SUP"], ["04_DC_Color", "COLOR"], ["04_DC_Cuenca", "CUENCA"], ["04_DC_Datum", "DATUM"], ["04_DC_FA_AnlQuimico", "ANL_QUIM"], ["04_DC_FA_AnlRadiactivo", "ANL_RD"], ["04_DC_FA_Fuente", "FUENTE"], ["04_DC_FA_QAQC", "QAQC"], ["04_DC_Geomorfologia", "GEOMORFO"], ["04_DC_Multimedia", "TIPO_M"], ["04_DC_Olor", "OLOR"], ["04_DC_Pendiente", "PENDIENTE"], ["04_DC_Proyecto", "CD_PROY"], ["04_DC_U_CE", "U_CE"], ["04_DC_U_Resist", "U_RESIS"], ["04_DC_U_Sal", "U_SAL"], ["04_DC_U_TDS", "U_TDS"], ["04_DC_Vertiente", "VERTIENTE"], ["04_DC_Zona", "ZONA"]

JSONS = os.path.join(BASE_DIR, 'json')
jsonFiles = os.listdir(JSONS)
jsonFiles.remove("domain")
pathDomain = os.path.join(JSONS, "domain")
listDomain = [os.path.join(pathDomain, x) for x in os.listdir(pathDomain)]

class CreateGDB:
    def __init__(self):
    	self.pathGdb = os.path.join(BASE_DIR, MODULE_NAME + ".gdb")
        # self.gdb = arcpy.CreateFileGDB_management(BASE_DIR, MODULE_NAME, "10.0")
        self.scratch = arcpy.env.scratchGDB

    def createFeatures(self):
        for j in jsonFiles:
            name = j.split(".")[-2]
            print name
            jtmp = arcpy.JSONToFeatures_conversion(os.path.join(JSONS, j), os.path.join(self.scratch, name))
            if j.split('_')[0] in ["GPT", "GPL", "GPO"]:
                ft = arcpy.CopyFeatures_management(os.path.join(self.scratch, name), os.path.join(self.pathGdb, name))
            elif j.split('_')[0] == "TB":
                tb = arcpy.JSONToFeatures_conversion(os.path.join(JSONS, j), os.path.join(self.scratch, 'a{:.5}'.format(str(uuid.uuid4()))))
                arcpy.TableToTable_conversion(tb, self.gdb, name)

    def makeDomain(self, jsonFile):
        with open(jsonFile, "r") as f:
            jx=f.read().decode("Windows-1252")
            data = json.loads(jx)
        df = pd.DataFrame.from_dict(data)
        domain = arcpy.CreateDomain_management(self.pathGdb, df['name'][0], "", "TEXT")
        print df['name'][0]
        for dom in df['codedValues']:
            val = [v for k,v in dom.items()]
            arcpy.AddCodedValueToDomain_management(self.pathGdb, df['name'][0], val[0], val[1])

    def createDomain(self):
        for i in listDomain:
            self.makeDomain(i)

    # def assignDomain(self):
    #     arcpy.env.workspace = self.pathGdb
    #     for j in jsonFiles:
    #         name = j.split(".")[-2]
    #         field_names = [f.name for f in arcpy.ListFields(name)]
    #         for x in listFieldsDomain:
    #             if x[0] in field_names:
    #                 arcpy.AssignDomainToField_management(name, x[0], x[1])
    #         print name

    def assignDomain(self):
        arcpy.env.workspace = self.pathGdb
        for j in jsonFiles:
            name = j.split(".")[-2]
            field_names = [f.name for f in arcpy.ListFields(name)]
            for x in listFieldsDomain:
                if x[0] in field_names:
                    arcpy.AssignDomainToField_management(name, x[0], x[1])
            print name


    def aaaa(self):
        # listaFT          = Lista de feature y tablas de la gdb
        # listnamesField   = Lista de nombre de los campos
        # listFieldsDomain = Lista [nombre dominio, campo al que pertenece]
        for m in listaFT:
            listnamesField = [x.name for x in arcpy.ListFields(m)]
            for y in listFieldsDomain:
                for z in listnamesField:
                    if y[1] == z:
                        arcpy.AssignDomainToField_management(m, y[1], y[0])


    def main(self):
        # print "#--------------------------"
        # print "Domains"
        # self.createDomain()
        # print "#--------------------------"
        # print "Features"
        # self.createFeatures()
        print "#--------------------------"
        print "Asignar Domains a features"
        self.assignDomain()
        

if __name__ == "__main__":
    poo = CreateGDB()
    poo.main()


# gdb = # Ruta de la gdb
# arcpy.env.workspace = gdb
# lista = arcpy.ListTables("*")
# listaJson = ["".join([x, ".json"]) for x in listaJson]
# for x in lista:
#     arcpy.AddField_management(x, "X","DOUBLE")
#     arcpy.AddField_management(x, "Y","DOUBLE")
#     ft = arcpy.MakeXYEventLayer_management(x, "X", "Y", "in_memory\test")
#     arcpy.FeaturesToJSON_conversion(ft, listaJson[lista.index(x)])
