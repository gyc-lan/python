import urllib.request
import os #创建文件夹
import random

def url_open(url):
    #访问url，获取url（基本语句）

    req = urllib.request.Request(url)
    req.add_header('User-Agent' , 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Mobile Safari/537.36')

    #添加代理
    proxies = ['61.135.217.7:80' , '182.88.179.69:8123' , '60.26.36.186:8118']

    proxy_support = urllib.request.ProxyHandler({'http' : random.choice(proxies)})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)
    
    
    response = urllib.request.urlopen(url) #必须是url
    html = response.read()
    return html

def get_page(url):
    html = url_open(url).decode('utf-8')
    
    #搜索page_num
    a = html.find("current-comment-page")
    b = html.find(']' , a) #从a开始寻找']'
    page_num = html[a+23:b]
    
    return page_num

def find_imgs(url):
    #图片的内容不能使用utf-8格式保存，需要使用Unicode编码
    html = url_open(url).decode('utf-8')
    imgs_list = []
    a = html.find('img src=')

    while a != -1: #a不存在时值为-1

        b = html.find('.jpg',a , a+255) #字符串的长度不会长过255,锁定b的搜索范围
        #可能出现其它格式的图片
        if b != -1:
            imgs_list.append(html[a+9:b+4])
        else:
            b = a + 9 #给未找到值得b一个值

        a = html.find('img src=' , b)
    
    return imgs_list

def save_img(folder, imgs_list):
    
    for each in imgs_list:
        filename = each.split('/')[-1]
        with open(filename , 'wb') as f:
            img = url_open(each)   #打开图片文件，获得图片的编码
            f.write(img) 
    
def download_mm(folder='OOXX' , page=1):

    os.mkdir(folder) #创建文件夹
    os.chdir(folder) #改变目录到指定目录
    url = "http://jandan.net/ooxx/"
    page_num = int(get_page(url))
    print(url)
    for i in range(page):
        
        #获取页面
        url = url + 'page-' + str(page_num) + '#comments'     
        #获得图片的内容保存到列表中
        imgs_list = find_imgs(url)
        #保存图片
        save_img(folder , imgs_list)
        page_num -= i


if __name__ == '__main__':
    download_mm()
        
    
