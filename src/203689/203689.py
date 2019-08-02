import urllib.request
import requests as req

# 1つ目の画像取得
# reqData1 = req.get('https://cdn.nissin.com/image?id=8833&s=720')
#
# with open('reqData1.jpg', 'wb') as file:
#     file.write(reqData1.content)
url1 = 'https://cdn.nissin.com/image?id=8833&s=720'
reqData1 = urllib.request.urlopen(url1).read()

with open('reqData1.jpg', 'wb') as file:
    file.write(reqData1)

# 2つ目の画像取得
url2 = 'https://catalog-p.meiji.co.jp/imageDisp.php?type=product&id=05997&dinimda=73342'
reqData2 = urllib.request.urlopen(url2).read()

with open('reqData2.jpg', 'wb') as file:
    file.write(reqData2)
