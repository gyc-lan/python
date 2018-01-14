import requests

url = 'http://charge.stage.yongche.org/v1/Charge/getFeeByServiceOrderIds'

params = {
    "service_order_id":"2005713741"
    }

r = requests.request("post", url, params=params)

print(r.text)
