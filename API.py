from ApiHelper import post

url_fcp_swagger = "https://fr1pslcmf05:8770/api/"
fcp_yc_definition = url_fcp_swagger+"pricing/Store/MarketData/YieldCurveDefinitions/"

yc_definition = {
    "name": "EUR_TEST",
    "currency": "EUR",
    "switchDates": [
        0,
        6
        ],
    "interpolationVariables": [
        "zeroCouponRate",
        "discountFactor",
        "zeroCouponRate"
        ],
    "interpolationMethods": [
        "flat",
        "linear",
        "flat"
        ],
    "zeroCouponFormula": "exponential",
    "zeroCouponBasis": "ACT/365.FIXED"
}

yc_def = post(url = fcp_yc_definition, json=yc_definition)