import requests
import json


def get(url):
    """REST CALL : GET"""
    reponse = requests.get(url, verify=False)
    if (reponse.ok):
        val = reponse.json()
    else:
        status = reponse.raise_for_status()
        val = "error : " + status
    reponse.close()
    return val


def delete(url,json ):
    """REST CALL : DELETE"""
    reponse = requests.delete(url, json=json,verify=False)
    if (reponse.ok):
        val = "currency deleted"
    else:
        status = reponse.raise_for_status()
        val = "error : " + status
    reponse.close()
    return val


def put(url, json):
    """REST CALL : PUT"""
    reponse = requests.put(url, json=json, verify=False)
    if (reponse.ok):
        val = json.loads(reponse.content)
    else:
        status = reponse.raise_for_status()
        val = "error : " + status
    reponse.close()
    return val

def post(url, json):
    """REST CALL : PUT"""
    reponse = requests.post(url, json=json, verify=False,headers={'Connection':'close'})
    if (reponse.ok):
        val= reponse.json()
    elif(reponse.status_code==400):
        val= reponse.text
    else:
        status = reponse.raise_for_status()
        val =  "error : " + status
    reponse.close()
    return val