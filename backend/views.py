from django.shortcuts import render

import requests


# Create your views here.

def api_authentication():
    headers = {
        'Authorization': 'Bearer ZG2NMXVEP0MD1CQP9CMQSE9K3X6X',
        'Content-Type': 'application/json'
    }

    response = requests.get('https://beta2.api.climatiq.io/emission-factors?source=BEIS&year=2021', headers=headers)

    print (response.text)
    #session = requests.Session()
    #session.headers
api_authentication()