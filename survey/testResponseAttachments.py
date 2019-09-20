import requests
import json
import os
import urllib2
import uuid

main_url = r'https://services1.arcgis.com/IOnDXYLCAWAfoO54/ArcGIS/rest/services/service_17c106ac35964f64be6708ff48abd974/FeatureServer/'
TB_FA_MULTIMEDIA = "3"
token = "JgCdqXDOVV4vrZI3NJ5TfbuzWjhmznVvfNMTxkBHRQVTzQJXJkWf_IV2bt7vwWJ0k2g4_ny7-AL3cRJjOHuilR3qKQn6j5MHDHsGFbDABXiJjsPowp8xVGJd8ScuF7rZqsTYvb0H0ps6_4qi1vEMxElA0SDtMD4FJ8ElXOvqlDg7QIp_13eqhnKRz025XHzta99viS558Tc9gtX6zAffqzgA2DDg8xz22_bgFpoE-WxtnuXoBY-fySotfixYQXYNgNfIthN-jbKT5-Icm03kU2_t0u1Xim-Rwn2dkV5Nxbw."

query_url_attach_Photos = ''.join([main_url, TB_FA_MULTIMEDIA, '/queryAttachments?token={}'.format(token)])

pathPhotos = r"D:\APPS\SURVEY\BDG_DGAR_FASUB\photos"

listaFotos = [[u'1314-01', u'83843c20-a3e9-4ad9-a958-ce8c3ae8c7cb'], [u'13154-001', u'9d629fe5-527e-4786-b256-241762e6e2cb'], [u'13154-001', u'f773aeed-b093-4b8f-8de2-20f0ee97513d'], [u'1314-', u'9747e096-e869-45c1-afba-5901730fd1f7']]

def responseAttachments():
    response = requests.post(
        query_url_attach_Photos,
        data={
            "definitionExpression": "1=1",
            "f": "pjson",
            'token': token
        }
    )
    res = json.loads(response.text)
    jsonresponse = res.get("attachmentGroups")
    return jsonresponse

jsonresponse = responseAttachments()

photos = []
for m in listaFotos:
    for n in jsonresponse:
        pgid = n.get("parentObjectId")
        if m[1] == n.get("parentGlobalId"):
            for j in n.get("attachmentInfos"):
                photos.append([pgid, j.get("id"), j.get("keywords")])

for x in photos:
    url_img = os.path.join(main_url, TB_FA_MULTIMEDIA, str(x[0]), "attachments",  "{}?token={}".format(x[1], token))
    filedata = urllib2.urlopen(url_img)
    image = filedata.read()
    f = open(os.path.join(pathPhotos, "{}{:.5}.jpg".format(x[2], str(uuid.uuid4()))),'wb')
    f.write(image)
    f.close()