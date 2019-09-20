import requests
import json


query = 'https://services1.arcgis.com/IOnDXYLCAWAfoO54/ArcGIS/rest/services/service_1d35578ed5e941a7b6797c257e30c14e/FeatureServer/0/query?token=p9UF_hPY11MRF-zFqbrxj_MyZBZhPCJ5sszXdvpJMR3-LSb3QOya8iUVCm9abqRJ06npfEKImcgdf9X2SSqZmaSk1lQAYpZEig1W65IfryWSY5uKDA1oKTNT4ErTr7d7Dqqw1MEm1GSE8Xgewih-1M-gRGtFyfftqdCVfLYoC1n7pP1Z9oe7MsnRFAITfBI5tIAcSrtgjyubQV9UaYw1ToVp3HDJIbTppRAbtVFuymqe7YRWun7nPNp6ANrMz6sF2MO84Bb6s95ZfcziluR5fmjZCt17ACs9WAIDRrxeBCw.'
fields = 'MIC_CUEN'

response = requests.post(
            query,
            data={
                'where': '1=1',
                'outFields': fields,
                'f': 'pjson'
            }
        )
res = json.loads(response.text)
print res
