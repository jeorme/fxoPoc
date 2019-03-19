from ApiHelper import *

url_fcp_swagger = "https://fr1pslcmf05:8770/api/"
url_fcc_swager = "https://fr1pslcmf05:8770/api/"
test = url_fcp_swagger+"#/default/get_pricing_Store_MarketData_FxRates"

### static data : Currency
fcp_Currency = url_fcp_swagger+"pricing/Store/StaticData/Currencies"
#fcp_Currency_delete = url_fcp_swagger+"pricing/Store/StaticData/Currencies/%24id%2Ftest"
currency_dom = { 'id': '$DOM', 'isoCode': 'DOM'}
currency_for = {'id' : '$FOR', 'isoCode' : 'FOR'}
print(post(url = fcp_Currency, json=currency_dom))
print(post(url=fcp_Currency,json=currency_for))
reponse = get(url = fcp_Currency)
file = open('output.json','w')
json.dump(reponse,file)
file.close()

###static data : currency pair
fcp_CurrencyPair = url_fcp_swagger+"pricing/Store/StaticData/CurrencyPairs"
#fcp_Currency_delete = url_fcp_swagger+"pricing/Store/StaticData/Currencies/%24id%2Ftest"
currency_pair = { 'id': '$FOR/$DOM', 'name': 'FOR/DOM'}
print(post(url = fcp_CurrencyPair, json=currency_pair))
#print(delete(url = fcp_Currency+"/id_test", json='id_test'))
reponse = get(url = fcp_CurrencyPair)
file = open('outputPair.json','w')
json.dump(reponse,file)
file.close()


