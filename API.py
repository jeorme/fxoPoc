from ApiHelper import post

url_fcp_swagger = "https://fr1pslcmf05:8770/api/"


# use the API unitary price to price a FXO with the corresponding measures
# we use the input defined by FCP and use the FCP pricer
# since the API is not defined we use the generic pricer and we set by default the non used parameter
def unitary(unitary_price):
    url_price = url_fcp_swagger + "pricing/price/"
    unitary_price["resultHandlerId"] = "Report"
    unitary_price["resultHandlerConfigId"] = "id-Default"
    unitary_price["marketDataProviderId"] = "PE_STORE_MDP"
    unitary_price["referenceCurrency"] = "id/USD"
    unitary_price["forceFiniteDifferences"]=False
    unitary_price["scenarioContexts"] = []
    unitary_price["scenarioContexts"].append({"outputCashflows": unitary_price["outputCashflows"]})
    unitary_price["scenarioContexts"].append({"outputPastCashflows": unitary_price["outputPastCashflows"]})
    unitary_price["scenarioContexts"].append({"resultsByLeg": unitary_price["resultsByLeg"]})
    unitary_price["scenarioContexts"].append({"id": "base"})
    unitary_price["scenarioContexts"].append({"measureGroupIds": unitary_price["measures"]["groupIds"]})
    unitary_price["perimeter"] = {"trade": {"tradeId": unitary_price["trade"]["tradeId"]["id"]}}
    return (post(url=url_price, json=unitary_price))


unitaryPrice ={
  "asOfDate": "2016-07-04",
  "pricingConfigId": "e26f34d7-8192-4264-b405-33b6b79afedb",
  "marketDataSetId": "id-Default",
  "pricingMethod": "THEORETICAL",
  "measures": {
    "groupIds": [
      "aa41a417-4327-476b-9868-fbfb4dead8c5"
    ]
  },
  "outputCashflows": True,
  "outputPastCashflows": True,
  "resultsByLeg": True,
  "forceFiniteDifferences": False,
  "trade": {
    "tradeId": {
      "id": "FXOptionVanilla_28",
      "version": "string",
      "draft": "string"
    }
  }
}

result = unitary(unitaryPrice)
print(result)