import urllib.request
import re
import os

def url_img(url):
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    html = response.read()
    return html

def pass_img(url):
    html = url_img(url).decode('utf-8')
    img = []
    #将正则表达式变异成Pattern对象
    pattern = re.compile(r'(src=").*(\.jpg")')
    img_1 = re.search(pattern, html)
    #当不存在时re.search()返回none
    while img_1:
        img.append('http://www.tuhao13.com' + img_1.group().split('"')[1])
        html = html[img_1.span()[1]:]
        img_1 = re.search(pattern, html)
    return img
    

def save_img(folder, img):
    for each in img:
        filename = each.split('/')[-1]
        html = url_img(each)
        with open(filename, 'wb') as f:     
            f.write(html)
    

def down_img(folder = 'imgs'):
    #创建文件夹
    os.mkdir(folder) #创建文件夹
    os.chdir(folder) #改变目录到指定目录

    #通过url获取
    url = "http://www.tuhao13.com/vod-type-id-4-pg-1.html"
    #获取图片的地址，并保存在列表中
    img = pass_img(url)
    #保存图片
    save_img(folder, img)

if __name__ == '__main__':
    down_img()
    
