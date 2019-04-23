from ApiHelper import post
from ConfigHelper import getPricingId

url_fcp_swagger = "https://fr1pslcmf05:8770/api/"
url_pricing_config = "https://fr1pslcmf05:8770/api/pricing/configs"
url_result_handler ="https://fr1pslcmf05:8770/api/pricing/report/result/Pricing"

# use the API unitary price to price a FXO with the corresponding measures
# we use the input defined by FCP and use the FCP pricer
# since the API is not defined we use the generic pricer and we set by default the non used parameter
def unitary(configName,aod,pricingMethod,marketDataSetId,resultHandlerId,referenceCurrency,resultHandlerConfigId,marketDataProviderId,perimeter,scenarioContexts):
    unitary_price = {}
    unitary_price["asOfDate"] = aod
    unitary_price["pricingMethod"] = pricingMethod
    unitary_price["marketDataSetId"] = marketDataSetId
    unitary_price["resultHandlerId"] = resultHandlerId
    unitary_price["resultHandlerConfigId"] = resultHandlerConfigId
    unitary_price["marketDataProviderId"] = marketDataProviderId
    unitary_price["referenceCurrency"] = referenceCurrency
    unitary_price["pricingConfigId"] = getPricingId(configName)
    unitary_price["perimeter"] = {"trade" : {"perimeterId": perimeter}}
    unitary_price["scenarioContexts"] = scenarioContexts
    url_price = url_fcp_swagger + "pricing/price/"
    post(url=url_price, json=unitary_price)
    return getResult()

def getResult(id="Pricing",dimensions="Id",measures="base_NPV"):
    url="https://fr1pslcmf05:8770/api/pricing/report/result/"+id
    resultHandler={}
    resultHandler["dimensions"]= [dimensions]
    resultHandler["measures"]= [measures]
    return post(url,json=resultHandler,isCsv=True)


scenarioContexts =[

    {
      "id": "base",
      "measureGroupIds": [
        "NPV"
      ]
    }

]
## what do we need :
##Kondor action :
## no ID defined directly
## asOfDate : from context (trade capture /report)
## pricingMethod : Theoretical (TO DO check if mandatory)

##with ID
## pricingConfigId : need a serivice to get the ID
## marketDataSetId : need a service to get the ID
## referenceCurrency : need a service to get the ID
## resultHandlerConfigID : need a service to get the ID
##resultHandlerID : need a service to get the ID
## marketDataPorviderID : need a service to the marketDataProvider
## measures : need to create a service to create the measure group (can we pass it directly)
## scenarioContext : need to create a service to get id
## perimeter : only ALL can we do it for one trade (need a creation of a perimeter)


result = unitary(configName="DEFAULT",aod="2016-07-04",pricingMethod="THEORETICAL",marketDataSetId="$id/DEFAULT",referenceCurrency="$id/USD",marketDataProviderId="PE_STORE_MDP",resultHandlerConfigId="Default",perimeter="ALL_FX_OPTION", scenarioContexts = scenarioContexts,resultHandlerId="Report")
