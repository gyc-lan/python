import requests

url = "http://charge.stage.yongche.org/v1/Charge/getFeeByServiceOrderIds"

querystring = {"service_order_id":"6493725490171555944"}

headers = {
    'cache-control': "no-cache",
    'postman-token': "1e17d42f-dbc3-ee71-4521-a65b86eb3eaf"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)