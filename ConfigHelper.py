from ApiHelper import get

def getPricingId(configName):
    urlConfig = "https://fr1pslcmf05:8770/api/pricing/configs"
    config = get(urlConfig)
    for item in config:
        if (item['name']==configName):
            return item["id"]
    return "error"

getPricingId("DEFAULT")
