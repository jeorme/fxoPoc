from ApiHelper import *

url_fcp_swagger = "https://fr1pslcmf05:8770/api/"
## url to create currency static data
fcp_currency_static = url_fcp_swagger+"pricing/Store/StaticData/Currencies/"
fcp_CurrencyPair = url_fcp_swagger+"pricing/Store/StaticData/CurrencyPairs/"
#url to push the Fx rate to the store
fcp_fxPair = url_fcp_swagger+"pricing/Store/MarketData/FxRates/"
#url for marketdata set
fcp_marketData_set = url_fcp_swagger+"pricing/marketDataSetIds"
fxPair = {
  "date": "2019-03-19",
  "marketSet": "DEFAULT",
  "name": "FOR/DOM",
  "value": 1.12
}
url_fxpair = post(url = fcp_fxPair, json=fxPair)

#urls for fcc

fcc_marketset = "http://fr1cslfcglo0056.misys.global.ad:30005/api/fcc/marketset"
MD = {  "description": "test_MarketSet",   "name": "testMS" }
#post MD
#add static :
#https://fr1cslfcglo0056.misys.global.ad:30005/doc/#/default/post_staticData_documents_v2_processdocuments