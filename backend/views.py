from django.shortcuts import render

import requests
#from dotenv import load_dotenv
import os

#load_dotenv()

#climatiq_API_KEY = os.getenv('climatiq_api_key')
# Create your views here.

def api_authentication(sector = None, category = None, source = None, region = None):
    year = "2021"
    source = "BEIS"
    url_params = "year=" + year

    
    if sector:
        url_params += "&sector=" + sector

    if category:
        url_params += "&category=" + category

    if source:
        url_params += "&source=" + source

    if region:
        url_params += "&region=" + region


    headers = {
        'Authorization': 'Bearer ZG2NMXVEP0MD1CQP9CMQSE9K3X6X', #+ climatiq_API_KEY,
        'Content-Type': 'application/json'
    }

    print ('https://beta2.api.climatiq.io/emission-factors/regions?' + url_params)

    try:
        response = requests.get('https://beta2.api.climatiq.io/emission-factors/regions?' + url_params, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as HTTPError:
        print(HTTPError)
    except requests.exceptions.ConnectionError as ConnectionError:
        print(ConnectionError)
    except requests.exceptions.Timeout as Timeout:
        print(Timeout)
    except requests.exceptions.RequestException as RequestException:
        print(RequestException)

    print (response.text)
    #session = requests.Session()
    #session.headers
api_authentication()