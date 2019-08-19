import os, requests
import json, uuid
import urllib2

_USER = 'publicadorapp'
_PASSWORD = 'publ1c4d0r'

def getToken():
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


url = 'https://services1.arcgis.com/IOnDXYLCAWAfoO54/ArcGIS/rest/services/service_407c8304a8c040b0806b3e422fb0f097/FeatureServer/8'
IDENTIFICADOR = "FICHA_FT"
PATH = r"D:\RYali\TDR5\2product\imgs"

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
            listImg.append([f["attributes"]["objectid"], f["attributes"][IDENTIFICADOR]])
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

    def readImg(self, url_img, path):
        filedata = urllib2.urlopen(url_img)
        image = filedata.read()
        img = open(os.path.join(PATH,"{}.png").format(path), "wb")
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
