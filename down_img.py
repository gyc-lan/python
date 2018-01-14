import urllib.request
import urllib.parse
import json
import time

while True:
    content = input("请输入要翻译的内容（输入"q!"退出）：")

    if content = 'q!':
        break
    
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom='
    data = {}

    data['i'] = content
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    #data['salt'] = '1509956704556'
    #data['sign'] = '2a02b4f3130dae9a693518304a6a10f5'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_CLICKBUTTION'
    data['typoResult'] = 'false'

    #解析代码，Unicode码编译为utf-8，因为data数据只能识别utf-8码
    data = urllib.parse.urlencode(data).encode('utf-8')

    req = urllib.request.Request(url , data)
    req.add_header('User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36')

    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')

    target = jaon.loads(html)
    target = target['translateResult'][0][0]['tgt']

    print(target)
    time.sleep(5)
