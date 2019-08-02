# import urllib.request
#
# url = 'http://militaryshop.jp/upload/save_image/IT-1454/IT-1454_00.JPG'
# save_name = 'test.jpg'
#
# tgt = urllib.request.urlopen(url).read()
#
# with open(save_name, mode='wb') as f:
#     f.write(tgt)

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
import os
import urllib.request

url = 'http://militaryshop.jp&#039'
url1 = '/upload/save_image/'
url2 = 'http://militaryshop.jp/products/detail.php?product_id=6985&#039'
# save_dr = '/Users/HIROKI/Desktop/python/'  # MacBook12用
# os.chdir(save_dr)  # カレントディレクトリの移動　/Users/HIROKI/Desktop/python

headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
}

r = requests.get(url2, headers=headers)

if r.status_code == requests.codes.ok:
    soup = BeautifulSoup(r.content, 'html5lib')

    title = (soup.select('#syouhin_title > h2'))  # ID,H2要素から抜き出し
    # title2 = title.string
    # print (soup.select("#two_maincolumn_right"))
    moji = soup.select('.main_comment')  # class要素から抜き出し
    moji = str(moji[0]).split('<!--START-->')[1]
    moji = moji.split('<!--END-->')[0]

    title = str(title[0]).split('<h2>')[1]
    title = title.split('</h2>')[0]

    title2 = title.split('【')[0]  # 商品タイトルのみ

    syouhin_bango = title.split('【商品番号 ')[1]
    syouhin_bango = syouhin_bango.split('】')[0]  # 商品番号のみ

    print(title)
    print(moji)
    print(syouhin_bango)
    print(title2)

    img = (soup.select('#undercolumn > img'))  # ID,H2要素から抜き出し
    img[0] = img[0].get("src")
    img[1] = img[1].get("src")

    img2 = (soup.select('.subtext > img'))  # ID,H2要素から抜き出

    for x in range(len(img2)):  # img2に入っているLIST数を回す
        img.append(img2[x].get("src"))  # img[x]にsrcを入れていく

    for x in range(len(img)):  # 画像srcを表示
        if img[x] == '/upload/save_image/':
            img[x] = ""  # 画像なしの場合はsrcを代入せずに空にして削除
    else:
        file_url = url + img[x]
    print(file_url)
    file_name = img[x].split(url1)[1]  # フォルダ以降抽出　例IT-1454/IT-1454_00.JPG
    print(file_name)
    file_url = file_name.split('/')  # 分割 listへ入れる
    # print(res)
    # res_kazu = len(res)  # フォルダとファイルの数（合計）
    dr1 = file_url[0]  # フォルダ名
    jpg_name = file_url[1]  # ファイル名
    print(dr1)
    print(jpg_name)

    os.makedirs(dr1, exist_ok=True)

    with open(save_dr + file_name, 'wb') as f:
        f.write(r.content)
