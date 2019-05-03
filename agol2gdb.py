import os, requests
import json, uuid
import arcpy

scratch = arcpy.env.scratchGDB
arcpy.env.overwriteOutput = True

gdb = r'E:\2019\TEMP.gdb'
nameFc = "SALUD"
url = 'https://sigrid.cenepred.gob.pe/arcgis/rest/services/Elementos_Expuestos/MapServer/1/query'

class RequestDataAGOL(object):
    def __init__(self):
        self.url = url
        self.listaOids = []
        self.pth = os.path.join(gdb, nameFc)
        if arcpy.Exists(self.pth) == True:
            if int(arcpy.GetCount_management(self.pth).getOutput(0)) != 0:
                arcpy.Delete_management(self.pth)
        
    def countOnly(self):
        response = requests.post(
            self.url,
            data = {
            'where': '1=1',
            'outFields': "*",
            'returnCountOnly': 'true',
            'f': 'pjson'
            }
        )
        res = json.loads(response.text)
        self.cantidad = res["count"]
        print(self.cantidad)

    def oidsOnly(self):
        response = requests.post(
            self.url,
            data = {
            'where': "1=1",
            'outFields': "*",
            'returnIdsOnly': 'true',
            'f': 'pjson'
            }
        )
        res = json.loads(response.text)
        self.listaOids.extend(res["objectIds"])
        self.listaOids = list(set(self.listaOids))

    def requestData(self):
        data = self.listaOids
        chunks = [data[x:x+1000] for x in xrange(0, len(data), 1000)]
        for n in chunks:
            print(len(n))
            n = ','.join([str(x) for x in n])
            response = requests.post(
                self.url,
                data = {
                'objectIds': n,
                'outFields': "*",
                'f': 'pjson'
                }
            )
            res = json.loads(response.text)
            feature = arcpy.AsShape(res, True)
            if arcpy.Exists(self.pth) == False:
                arcpy.CopyFeatures_management(feature, self.pth)
            else:
                arcpy.Append_management(feature, self.pth, 'NO_TEST')

    def main(self):
        self.countOnly()
        self.oidsOnly()
        self.requestData()

if __name__ == '__main__':
    poo = RequestDataAGOL()
    poo.main()