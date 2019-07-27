import urllib.request

url = 'http://militaryshop.jp/upload/save_image/IT-1454/IT-1454_00.JPG'
save_name = 'test.jpg'

tgt = urllib.request.urlopen(url).read()

with open(save_name, mode='wb') as f:
    f.write(tgt)
