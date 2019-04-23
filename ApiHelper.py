import requests
import json
import pandas as pd
#helper
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


def delete(url ):
    """REST CALL : DELETE"""
    reponse = requests.delete(url,verify=False)
    if (reponse.ok):
        val = "data deleted"
    else:
        status = reponse.raise_for_status()
        val = "error : " + status
    reponse.close()
    return val


def put(url, json):
    """REST CALL : PUT"""
    reponse = requests.put(url, json=json, verify=False)
    if (reponse.ok):
        val = "build"
    else:
        status = reponse.raise_for_status()
        val = "error : " + status
    reponse.close()
    return val

def post(url, json,isCsv=False):
    """REST CALL : POST"""
    reponse = requests.post(url, json=json, verify=False,headers={'Connection':'close'})
    if(reponse.ok):
        if(reponse.status_code==201):
            val = reponse.headers._store['location'][1]
        else:
            if isCsv:
                lines = reponse.text.splitlines()
                val = []
                for item in range(1,len(lines)):
                    id,npv = lines[item].split(";")
                    val.append({"id" : id,"npv" : npv})
            else:
                val = reponse.json()
    elif(reponse.status_code==400):
        val= reponse.text
    else:
        status = reponse.raise_for_status()
        val =  "error : " + status
    reponse.close()
    return val