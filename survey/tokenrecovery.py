import requests

user = 'publicadorapp'
password = 'publ1c4d0r'

def getToken():
    _URL = "https://www.arcgis.com/sharing/generateToken"
    
    data = {
        'username': user,
        'password': password,
        'referer': "http://ingemmet-peru.maps.arcgis.com",
        'request': 'gettoken',
        'f': 'json'
    }

    response = requests.post(_URL, data=data)
    response = response.json()
    token = response.get('token', 0)
    return token