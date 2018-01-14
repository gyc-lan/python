import urllib.request
import random

url = 'http://www.whatismyip.com.tw'

ip_list = ['27.46.74.26:9999' ,'112.67.183.75:9797' ,'61.135.217.7:80']


proxy_support = urllib.request.ProxyHandler({'http' : random.choice(ip_list)})

opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36')]

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

print(html)


