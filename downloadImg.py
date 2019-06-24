import os, requests
import json, uuid
import urllib2
# token = 'rpt_Zd9ooapP-6AbayixwQvCcTs16Y5FAx5b6a-C6msEZKWyrjcUNvKmNF8KhyDVwL3KZoLO45IsLuIbmGobqNgem7i6Jk8xUX9SMvKtPF9dhPlX4zdp5Y44NvCBtMc3d79U0SGiW8enUq704UqeF4mEJ1HWAJHUGGFQGWfg-B4fm8uW_LqIXVnVPhjvqJR3g3k-F1hHaEB51-2L8wOzRtYJIAetQ2CAe4WLJ6joizaNSDOP9_dOLV5NxSD-VZV9eNWISVsVsm6SqLaFQMY4hazy8YzrdBtyVr1ppdbiImw.'
# 'https://services1.arcgis.com/IOnDXYLCAWAfoO54/ArcGIS/rest/services/service_407c8304a8c040b0806b3e422fb0f097/FeatureServer/8/33/attachments/26?token='

_USER = 'publicadorapp'
_PASSWORD = 'publ1c4d0r'

def getToken():
    '''
    :return: Devuelve el token unico por modulo y maquina 
    '''
    _URL = "https://www.arcgis.com/sharing/generateToken"
    data = {
        'username': _USER,
        'password': _PASSWORD,
        'referer': "http://ingemmet-peru.maps.arcgis.com",
        'request': 'gettoken',
        'f': 'json'
    }
    response = requests.post(_URL, data=data)
    response = response.json()
    token = response.get('token', 0)
    return token

token = getToken()
# Servicio de fotos
url = 'https://services1.arcgis.com/IOnDXYLCAWAfoO54/ArcGIS/rest/services/service_407c8304a8c040b0806b3e422fb0f097/FeatureServer/8'

class downloadImg(object):
    def __init__(self):
        self.url = url

    def requestData(self):
        response = requests.post(
                self.url + "/query" ,
                data = {
                'where': "1=1",
                'outFields': "*",
                'f': 'pjson',
                'token': token
                }
            )
        res = json.loads(response.text)
        return res

    def readDataPhotos(self):
        res = self.requestData()
        print("\n")
        listImg = []
        for f in res["features"]:
            listImg.append([f["attributes"]["objectid"], f["attributes"]["FICHA_FT"]])
        return listImg

    def readUrlPhotos(self):
        response = requests.post(
                self.url + "/queryAttachments" ,
                data = {
                'definitionExpression': "objectid>0",
                'f': 'pjson',
                'token': token
                }
            )
        res = json.loads(response.text)
        listaUrlImg = []

        for f in res["attachmentGroups"]:
            poi = f["parentObjectId"]
            for i in f["attachmentInfos"]:
                fid = i["id"]
                url_img = os.path.join(self.url, str(poi), "attachments", "{}?token={}".format(fid, token))
                listaUrlImg.append([poi, fid ,url_img])
        return listaUrlImg                
        # filedata = urllib2.urlopen(url_img)
        # image = filedata.read()
        # row = [image, x[2], x[3], x[0], x[1]]

    def readImg(self, url_img, path):
        filedata = urllib2.urlopen(url_img)
        image = filedata.read()
        img = open(os.path.join(r"D:\RYali\TDR5\2product\imgs","{}.png").format(path), "wb")
        img.write(image)
        img.close()

    def main(self):
        listImg = self.readDataPhotos()
        listaUrls = self.readUrlPhotos()
        print(listImg)
        print(listaUrls)
        listaImgs = []
        for x in listImg:
            for y in listaUrls:
                if x[0] == y[0]:
                    if x[1] == None:
                        x[1] = x[0]
                    y.append(x[1])
                    listaImgs.append(y)

        for img in listaImgs:
            self.readImg(img[2], img[3])

if __name__ == '__main__':
    poo = downloadImg()
    poo.main()
